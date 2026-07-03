from bot.cli import get_args
from bot.orders import place_market_order, place_limit_order

args = get_args()

try:

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price    : {args.price}")

    print("===================================\n")

    if args.type == "MARKET":

        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        if args.price is None:
            raise ValueError("LIMIT order requires --price")

        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("✅ Order Placed Successfully\n")

    print("Order ID       :", response["orderId"])
    print("Status         :", response["status"])
    print("Executed Qty   :", response["executedQty"])
    print("Average Price  :", response.get("avgPrice", "N/A"))

except ValueError as ve:
    print("Validation Error:", ve)
except Exception as e:
    print("API Error:", e)