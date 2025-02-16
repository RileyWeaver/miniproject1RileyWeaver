## INF601 - Advance Programming in Python
## Riley Weaver
## Mini Project 01

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
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

today = datetime.now()

ten_days_ago = today - timedelta(days=15)

# Microsoft, Ubisoft, Netflix, Nvidia, United Airlines using different ones from the video
myTickers = ["MSFT" , "UBSFY", "NFLX", "NVDA", "UAL"]

#I followed along with the video provided to better understand the process
for ticker in myTickers:
    result = yf.Ticker(ticker)
    hist = result.history(start= ten_days_ago, end =today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        myArray = np.array(last10days)
        max_price = myArray.max() + (myArray.max()*.05)
        min_price = myArray.min() - (myArray.min()*.05)
        plt.plot(myArray)
        plt.xlabel('Data Points')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price ))
        # Uppercase looked better to me
        plt.title(f" {ticker} LAST 10 DAYS")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")