from trade.modules.trade_operations import Operations
from trade.modules.session import Session
from flask import request, Blueprint, current_app
import logging
import json
import requests
from datetime import datetime

log = logging.getLogger(__name__)
bp = Blueprint('positions', __name__)

@bp.route('/positions', methods=['GET'])
def get_positions():
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

@bp.route('/positions', methods=['PUT'])
def update_position():
    if request.is_json:
        profit_distance = None
        profit_level = None
        stop_level = None
        
        data = request.json
        deal_id = data["dealId"]
        if 'profitDistance' in data:
            profit_distance = data['profitDistance']
        if 'profitLevel' in data:
            profit_level = data['profitLevel']
        if 'stopLevel' in data:
            stop_level = data['stopLevel']

        session = Session.get_last_session_keys()
        
        request_endpoint = f"{current_app.config.get('API_URL')}/positions/{deal_id}"
        
        headers = {
            'X-SECURITY-TOKEN': session['X-SECURITY-TOKEN'], 
            'CST': session['CST']
            }
        
        params = {
            'profitDistance': profit_distance,
            'profitLevel': profit_level,
            'stopLevel' : stop_level
            }

        log.debug(f'Endpoint: {request_endpoint}')
        log.debug(f'Headers: {headers}')
        api_request = requests.put(request_endpoint, headers=headers, json=params)
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