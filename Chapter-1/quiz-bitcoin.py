
import yfinance
import matplotlib.pyplot as plt
price = yfinance.download(["BTC-USD"], start="2014-01-01")["Adj Close"]
price.plot()
plt.show()
price.tail(1)
