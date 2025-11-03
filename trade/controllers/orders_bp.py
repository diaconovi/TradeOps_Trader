from trade.modules.trade_operations import Operations
from trade.modules.session import Session
from flask import request, Blueprint, current_app
import logging
import json
import requests
from datetime import datetime

log = logging.getLogger(__name__)
bp = Blueprint('orders', __name__)

@bp.route('/orders', methods=['GET'])
def get_orders():
    session = Session.get_last_session_keys()
    
    request_endpoint = f"{current_app.config.get('API_URL')}/workingorders"
    
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
    else:
        return api_request.status_code

@bp.route('/orders', methods=['POST'])
def place_order_buy():
    if request.is_json:
        order_type = "LIMIT"
        operation = "BUY" 
        profit_distance = None
        profit_level = None
        stop_level = None
        
        data = request.json
        epic = data['epic']
        size = data['size']
        price = data['price']
        if 'profitDistance' in data:
            profit_distance = data['profitDistance']
        if 'profitLevel' in data:
            profit_level = data['profitLevel']
        if 'stopLevel' in data:
            stop_level = data['stopLevel']
        if 'type' in data:
            order_type = data['type']

        session = Session.get_last_session_keys()
        
        request_endpoint = f"{current_app.config.get('API_URL')}/workingorders"
        
        headers = {
            'X-SECURITY-TOKEN': session['X-SECURITY-TOKEN'], 
            'CST': session['CST']
            }
        
        params = {
            'epic': epic,
            'direction': operation,
            'size': size,
            'level': price,
            'type': order_type,
            'profitDistance': profit_distance,
            'profitLevel': profit_level,
            'stopLevel' : stop_level
            }

        log.debug(f'Endpoint: {request_endpoint}')
        log.debug(f'Headers: {headers}')
        api_request = requests.post(request_endpoint, headers=headers, json=params)
        Session.update_session_expire()

        if api_request.status_code == 200:
            request_json = api_request.json()
            
            return json.dumps(request_json)
        else:
            request_json = api_request.json()
            with open("error.log", "a") as f:
                f.write(f"{datetime.now()}\n")
                f.write(f"  request error: {request_json}\n")
                f.write(f"  request error: {request_endpoint}\n")
                f.write(f"  body: {json.dumps(params)}\n")
                f.write(f"  headers: {json.dumps(headers)}\n")
            return json.dumps(request_json)

    else:
        return 'Not a json body'
    
