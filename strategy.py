# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:06:31 2018

@author: Ars
"""

import python_client
#import talib
from time import sleep

symbol = 'EURUSD'
timeframe = 'H1'
start = 0
end = 2000
period = 96
stopLoss = 500
takeProfit = 1000
order = ''

trade = python_client.zmq_python()

while True:
    try:
        prices = trade.get_data(symbol='EURUSD', timeframe='H1', start_bar=start, end_bar=end)
        #SMA = talib.SMA(prices, timeperiod=period)
        print("Current price: {} \nSMA: {}".format(prices[-1]))

        if order != 'Buy' and order != 'Sell':
            if (prices[-1] > prices[-2]):
                order = 'Buy'
                trade.buy_order(symbol=symbol, stop_loss=stopLoss, take_profit=takeProfit)

            else:
                if (prices[-1] < prices[-2]):
                    order = 'Sell'
                    trade.sell_order(symbol=symbol, stop_loss=stopLoss, take_profit=takeProfit)

        if order == 'Buy':
            order = ''
            trade.close_buy_order()

        else:
            if order == 'Sell' :
                order = ''
                trade.close_sell_order()
    except:
        continue

    sleep(100)




