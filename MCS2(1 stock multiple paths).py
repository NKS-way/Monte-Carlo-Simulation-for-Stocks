import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("AUBANK.BO", period = "1y")
prices = data['Close']

returns = prices.pct_change().dropna()

mu = np.mean(returns)
sigma = np.std(returns)

num_sim = 1000
days = 252

all_sim = []

for i in range(num_sim):
    sim_returns = np.random.normal(mu,sigma,days)

    price = prices.iloc[-1]
    sim_prices = [price]

    for r in sim_returns:
        price = price * (1+r)
        sim_prices.append(price)
    
    all_sim.append(sim_prices)

for sim in all_sim:
    plt.plot(sim, alpha=1)

plt.title("Monte Carlo Simulation (1000 paths)")
plt.show()
final_prices = [sim[-1] for sim in all_sim]
mean_price = np.mean(final_prices)
p5 = np.percentile(final_prices, 5)
p95 = np.percentile(final_prices, 95)

print(p5,p95,mean_price)
