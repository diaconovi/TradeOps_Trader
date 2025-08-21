from flask import current_app
import requests
from datetime import datetime

class Session:
    security_key = ''
    cst = ''
    session_datetime = datetime.now()
    session_manager_endpoint = ''
    expiration = 0

    def __init__(self, context):
        self.context = context
        Session.session_manager_endpoint = f'{context.config.get('SESSION_MANAGER_URL')}:{context.config.get('SESSION_MANAGER_PORT')}'
        Session.expiration = context.config.get('SESSION_EXPIRATION')
        Session.refresh_session()

    @classmethod
    def refresh_session(cls):
        session_endpoint = f'{Session.session_manager_endpoint}/session/last'

        api_request = requests.post(session_endpoint)
        if api_request.status_code == 200:
            session_json = api_request.json()
            Session.security_key = session_json['X-SECURITY-TOKEN']
            Session.cst = session_json['CST']
            Session.session_datetime = datetime.strptime(session_json['createdAt'],'%Y-%m-%d %H:%M:%S.%f')
            return {'X-SECURITY-TOKEN': Session.get_security_key(), 'CST': Session.get_cst()}
        else:
            raise Exception('Cant get Session')

    @classmethod
    def get_security_key(cls):
        return cls.security_key
    
    @classmethod    
    def get_cst(cls):
        return cls.cst
    
    def get_last_session_keys():
        if (datetime.now() - Session.session_datetime).total_seconds() < Session.expiration:
            print('stored date')
            return {'X-SECURITY-TOKEN': Session.get_security_key(), 'CST': Session.get_cst()}
        else:
            print('refresh me')
            print(Session.security_key)
            print(Session.cst)
            return Session.refresh_session()
    
    def update_session_expire():
          update_endpoint = f'{Session.session_manager_endpoint}/session/update'
          headers = {'Content-Type':'application/json'}
          body = {'X-SECURITY-TOKEN': Session.security_key}
          requests.patch(update_endpoint, headers=headers, json=body)