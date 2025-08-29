from trade.modules.session import Session
from trade.modules.mongo_client import MongoDBClient
from trade.modules.trade_operations import Operations
from trade.controllers.orders_bp import bp as OrdersBp
from trade.controllers.positions_bp import bp as PositionsBp
from flask import Flask, current_app
import json
import logging
import sys

def init_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_pyfile('./config.py')
    # Switch API_URL based of DEMO_ACCOUNT valur
    if app.config['DEMO_ACCOUNT'] == True:
        app.config['API_URL'] = app.config['DEMO_ENDPOINT']
    else:
        app.config['API_URL'] = app.config['BASE_ENDPOINT']
    
    # Logger
    try:
        numeric_level = getattr(logging, app.config['DEBUG_LEVEL'])
    except AttributeError:
        raise ValueError(f"Invalid log level: {app.config['DEBUG_LEVEL']}")
    
    logging.basicConfig(stream=sys.stdout, level=numeric_level)

    #Init Session
    with app.app_context():
        Session(current_app)
        Operations(current_app)
        MongoDBClient.set_client(current_app)

    app.register_blueprint(OrdersBp)
    app.register_blueprint(PositionsBp)

    @app.route("/")
    def main_route():
        main_json = {
            'Module': 'Trader',
            'version': 'TBD'
            }
        return main_json

    @app.route("/configuration")
    def configuration():
        return json.dumps(app.config, indent=4, sort_keys=True, default=str)
    
    return app