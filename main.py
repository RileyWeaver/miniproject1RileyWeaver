## INF601 - Advance Programming in Python
## Riley Weaver
## Mini Project 1

'''
INF601 - Programming in Python
Assignment: mini project 1
I,     Riley Weaver    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty,
 including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance
 and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result
 in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement,
 I acknowledge my commitment to upholding the principles of academic integrity.
'''
##Import Package
import yfinance as yf
import pprint
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import copy

today = datetime.now()

ten_days_ago = today - timedelta(days=15)

# Microsoft, Ubisoft, Netflix, Nvidia, United Airlines
mytickers = ["MSFT" , "UBSFY", "NFLX", "NVDA", "UAL"]


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(start= ten_days_ago, end =today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Data Points')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price ))
        plt.title(f" {ticker.upper()} last 10 days")
        plt.show()
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")



# get all stock info
#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="1mo")

#pprint.pprint(hist)