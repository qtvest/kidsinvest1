import yfinance
import matplotlib.pyplot as plt
AAPL = yfinance.download(["AAPL"], start="2011-01-04", end="2021-01-04")
AAPL
price = AAPL["Adj Close"]
price.plot()
plt.show()

