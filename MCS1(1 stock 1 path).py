import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("AUBANK.BO", period = "1y")
prices = data['Close']

returns = prices.pct_change().dropna()

mu = np.mean(returns)
sigma = np.std(returns)

days = 252
sim_returns = np.random.normal(mu,sigma,days)

price = prices.iloc[-1]

sim_prices = [price]

for r in sim_returns:
    price = price*(1+r)
    sim_prices.append(price)

plt.figure()

plt.subplot(2,1,1)
plt.plot(sim_prices)
plt.title("Simulated Prices")

plt.subplot(2,1,2)
plt.plot(sim_returns)
plt.title("Simulated Returns")

plt.show()