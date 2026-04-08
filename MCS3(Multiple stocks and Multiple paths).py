import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

stocks = ["AAPL", "GOOG", "MSFT", "NVDA"]
data = yf.download(stocks, period = "3y")['Close']
returns = data.pct_change().dropna()

mu = returns.mean()
cov = returns.cov()

num_sim = 1000
days = 756
all_sim = []

for i in range(num_sim):
    prices = data.iloc[-1].values 
    sim_prices = [prices]

    for j in range(days):
        sim_returns = np.random.multivariate_normal(mu, cov)

        prices = prices * (1 + sim_returns)
        sim_prices.append(prices)

    all_sim.append(sim_prices)

for sim in all_sim:
    plt.plot([p[0] for p in sim], alpha=0.1)  # plotting the 1000 paths for AAPL(Change the ticker for whatever stock needed)

plt.title("Monte Carlo Simulation (AAPL)")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()

final_prices = [sim[-1][0] for sim in all_sim]  # final prices distribution
plt.hist(final_prices, bins=50)
plt.title("Final Price Distribution (AAPL)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

mean = np.mean(final_prices)
p5 = np.percentile(final_prices, 5)
p95 = np.percentile(final_prices, 95)

print("Expected Price:", mean)     # Mean final price
print("Worst 5%:", p5)             # Price less than x in 5% cases(Worst)
print("Best 5%:", p95)             # Price more than x in 5% cases(Best)

plt.hist(final_prices, bins=50)
plt.axvline(mean, linestyle='dashed', label='Mean')
plt.axvline(p5, linestyle='dashed', label='5th %')
plt.axvline(p95, linestyle='dashed', label='95th %')
plt.legend()
plt.show()

weights = np.array([0.25, 0.25, 0.25, 0.25])        # Computing the final portfolio values with 25% allocation of each stock
portfolio_values = []

for sim in all_sim:
    final_prices = sim[-1]
    portfolio_value = np.dot(weights, final_prices)
    portfolio_values.append(portfolio_value)

plt.hist(portfolio_values, bins=50)
plt.title("Portfolio Value Distribution")
plt.xlabel("Portfolio Value")
plt.ylabel("Frequency")
plt.show()

print("Portfolio Expected:", np.mean(portfolio_values))
print("Portfolio Worst 5%:", np.percentile(portfolio_values, 5))

plt.scatter(returns['AAPL'], returns['MSFT'])       # Specific Correlation between two stocks(moving together or opposite)
plt.xlabel("AAPL")                                  # Change the ticker for correlation between other stocks
plt.ylabel("MSFT")
plt.show()