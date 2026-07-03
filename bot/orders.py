from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"MARKET ORDER -> Symbol:{symbol}, Side:{side}, Quantity:{quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"API Response: {order}")

        return order

    except Exception as e:
        logger.error(str(e))
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT ORDER -> Symbol:{symbol}, Side:{side}, Qty:{quantity}, Price:{price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"API Response: {order}")

        return order

    except Exception as e:
        logger.error(str(e))
        raise