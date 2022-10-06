import yfinance
import matplotlib.pyplot as plt
BTC = yfinance.download(["BTC-USD"], start="2015-01-01", end="2022-06-30")
BTC["Adj Close"].plot()
plt.show()
