

import alpaca_trade_api as tradeapi
import numpy as np
import requests

# Alpaca API credentials
api_key = 'PKAFI9XFK0O6VYL8JUND'
api_secret = 'GUuoMmZZQ3r5UReJCTtsKsKYCKH2xK9CyWTfQHYm'
base_url = 'https://paper-api.alpaca.markets'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

HEADERS ={'APCA-API-KEY-ID': api_key , 'APCA-API-SECRET-KEY':api_secret }

def get_account():
  r = requests.get(ACCOUNT_URL, headers= HEADERS)
  return json.loads(r.content)

def create_order(symbol,qty,side,type,time_in_force):
  data={
      "symbol":symbol,
       "qty":qty,
       "side":side,
       "type":type,
       "time_in_force":time_in_force
  }
  r = requests.post(ORDERS_URL, json=data ,headers= HEADERS)
  return json.loads(r.content)





api_v2 = tradeapi.REST(api_key, api_secret, api_version="v2")
bars = api_v2.get_bars(["AAPL"], '1Min', limit=1)




# Parameters
symbol = 'AAPL'
bb_length = 20
bb_mult = 2.0
fib_levels = [0.236, 0.382, 0.618, 0.786, 0.886, 1.0]
stop_loss = 1.0
take_profit = 2.0

# Initialize API
api = tradeapi.REST(api_key, api_secret, base_url)

# Get last 20 prices for symbol
# bars = api.get_bars(symbol, 'day', limit=20)[symbol]


close_price_data = [bar.c for bar in bars]

# Bollinger Bands
close = np.array(close_price_data)
upper, middle, lower = talib.BBANDS(close, timeperiod=bb_length, nbdevup=bb_mult, nbdevdn=bb_mult)

# Fibonacci Retracement Levels
high_price_data = [bar.h for bar in bars]
low_price_data = [bar.l for bar in bars]
high = np.array(high_price_data)
low = np.array(low_price_data)
price_range = np.max(high[-20:]) - np.min(low[-20:])
fib_levels_price = high[-20:] - price_range * np.array(fib_levels)

# Entry and Exit Conditions
long_condition = (close[-1] > upper[-1] and close[-2] < upper[-2] and close[-1] > middle[-1])
short_condition = (close[-1] < lower[-1] and close[-2] > lower[-2] and close[-1] < middle[-1])
stop_loss_price = close[-1] * (1 - stop_loss/100)
take_profit_price = close[-1] * (1 + take_profit/100)

if long_condition:
    # Submit a market order to buy 10 shares of AAPL
    api.create_order(
        symbol=symbol,
        qty=10,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if short_condition:
    # Submit a market order to sell 10 shares of AAPL
    api.create_order(
        symbol=symbol,
        qty=10,
        side='sell',
        type='market',
        time_in_force='gtc'
    )

# Plotting
# plot the Bollinger Bands and Fibonacci retracement levels on the chart for visual analysis
