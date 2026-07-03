import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading Symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        type=str,
        required=True,
        choices=["BUY", "SELL"],
        help="Order Side"
    )

    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        required=False,
        help="Limit Order Price"
    )

    return parser.parse_args()