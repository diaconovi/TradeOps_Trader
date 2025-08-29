import requests

class Operations:

    def __init__(self, context):
        self.context = context
        Operations.api_url = f'{context.config.get('API_URL')}'

    def get_current_orders():
        return ''
    
    def get_current_positions():
        return ''
    
    def place_order_buy(epic, size, price, profitDistance = None, stopLevel = None):
        direction = "BUY"
        order_type = "LIMIT"
        return ''

    def update_order():
        return ''
    
    def delete_order():
        return ''
    
    def update_positions():
        return ''
    
    def delete_position():
        return ''