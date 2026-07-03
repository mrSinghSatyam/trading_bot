# Binance Futures Testnet Trading Bot

A Python-based CLI application that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M). The project demonstrates API integration, command-line argument parsing, input validation, logging, and error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL orders
- Command Line Interface (CLI) using argparse
- Input validation
- Logging of API requests, responses, and errors
- Exception handling for invalid input and API failures
- Modular and reusable project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading.log
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.10 or above
- Binance Futures Testnet Account
- Binance Futures Testnet API Key
- Internet Connection

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/trading_bot.git

cd trading_bot
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.


---

## Running the Application

### Place a MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example

```bash
python main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.002
```

---

### Place a LIMIT Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

Example

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 60000
```

---

## Sample Output

```
========== ORDER REQUEST ==========
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001
===================================

Order Placed Successfully

Order ID       : 18649267690
Status         : NEW
Executed Qty   : 0.0000
Average Price  : N/A
```

---

## Log File

All API requests, responses, and errors are stored in:

```
logs/trading.log
```

Example

```
INFO - MARKET ORDER -> Symbol: BTCUSDT
INFO - API Response:
{
   ...
}
```

---

## Error Handling

The application handles:

- Invalid order type
- Invalid trading side
- Invalid quantity
- Missing LIMIT price
- Binance API errors
- Network failures
- Authentication failures

---

## Assumptions

- Binance Futures Testnet API credentials are valid.
- Only USDT-M Futures trading is supported.
- Internet connection is available.
- Orders are executed on the Binance Futures Testnet only.
- User provides valid trading symbols.

---

## Technologies Used

- Python 3
- python-binance
- argparse
- python-dotenv
- logging

---

## Author

**Satyam Singh**

B.Tech Information Technology

GitHub: https://github.com/mrSinghSatyam