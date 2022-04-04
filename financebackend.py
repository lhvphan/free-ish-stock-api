'''
    File name: financebackend.py
    Author: lhvphan
    Email: lhvphan@gmail.com
    Date created: April 3, 2022
    Python Version: 3.8
    Description: call yahoo finance to get ticker information, returns json object
'''

import yfinance as yf
import json

class FinanceBackend:
    
    def getone(self, input):
        """
        function getone: get information for one stock
        :param self: self object
        :param input: expect stock ticker type string
        :return returnval: json object
        """

        # get info for stock symbol
        print("stock symbol input: %s" % input)
        stock = yf.Ticker(input)

        # create temp object (dict)
        x = {
            "symbol": stock.info["symbol"],
            "price": stock.info["currentPrice"],
            "high": stock.info["fiftyTwoWeekHigh"],
            "low": stock.info["fiftyTwoWeekLow"]
        }

        # convert object to json object and return
        returnval = json.dumps(x)
        print("stock is (json): %s" % returnval)
        return returnval


    def getmany(self, input):
        """
        function getmany: get information for more than one stock
        :param self: self object
        :param input: expect stock tickers type json object
        :return returnval: json object
        """

        # create empty object (dict) array
        returnval = []

        # loop though each key pair
        for key in input:
            #print(key, ":", input[key])
            stock = yf.Ticker(input[key])

            # create temp object (dict)
            x = {
                "symbol": stock.info["symbol"],
                "price": stock.info["currentPrice"],
                "high": stock.info["fiftyTwoWeekHigh"],
                "low": stock.info["fiftyTwoWeekLow"]
            }
            print("%s : %s" % (key,x))
            returnval.append(x)

        # convert dict array to json and return
        returnval = json.dumps(returnval)
        print("Stocks are (json): %s" % returnval)
        return returnval