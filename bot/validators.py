def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are supported.")

def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("LIMIT orders require a valid price.")