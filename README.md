# Monte Carlo Simulation for Stock & Portfolio Analysis

## Overview

This project implements a Monte Carlo simulation to model and analyze the future behavior of stock prices and portfolios using historical market data.

Instead of predicting a single outcome, the simulation generates multiple possible future scenarios to understand uncertainty, risk, and expected returns.

---

## Features

* Multi-stock simulation using real market data
* Monte Carlo simulation with 1000+ paths
* Correlation-aware modeling using covariance matrix
* Visualization of simulated price paths
* Distribution analysis of final stock prices
* Portfolio simulation with customizable weights
* Risk analysis using percentiles (5% worst-case, 95% best-case)

---

## Methodology

1. Fetch historical stock data using yfinance
2. Calculate daily returns
3. Compute mean returns and covariance matrix
4. Generate random returns using multivariate normal distribution
5. Simulate future price paths
6. Run multiple simulations to model uncertainty
7. Analyze results using statistical metrics

---

## Results

The simulation provides:

* Expected future price of stocks
* Downside risk (5th percentile)
* Upside potential (95th percentile)
* Portfolio-level risk and return insights

---

## Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* yFinance

---

## Future Improvements

* Implement Geometric Brownian Motion (GBM)
* Add interactive dashboard (Streamlit)
* Optimize simulation using vectorization
* Integrate real-time data

---
