from trade.modules.trade_operations import Operations
from trade.modules.session import Session
from flask import request, Blueprint, current_app
import logging
import json
import requests

log = logging.getLogger(__name__)
bp = Blueprint('positions', __name__)

@bp.route('/positions', methods=['GET'])
def get_orders():
    session = Session.get_last_session_keys()
    
    request_endpoint = f"{current_app.config.get('API_URL')}/positions"
    
    headers = {
        'X-SECURITY-TOKEN': session['X-SECURITY-TOKEN'], 
        'CST': session['CST']
        }
    
    log.debug(f'Endpoint: {request_endpoint}')
    log.debug(f'Headers: {headers}')
    api_request = requests.get(request_endpoint, headers=headers)
    Session.update_session_expire()

    if api_request.status_code == 200:
        request_json = api_request.json()
        
        return json.dumps(request_json)


    positions = Operations.get_current_orders()
    return positions
