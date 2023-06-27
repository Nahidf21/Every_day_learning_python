import numpy as np
import pandas as pd
from scipy.stats import norm

R = 18  # selling price
C = 12  # cost price
S = 9  # salvage value
Qrange = list(range(40, 51))  # range of possible Q values

# given demand data
vd = [42,45,40,46,43, 43, 46, 42, 44, 43, 47, 41,
    41, 45,51,45,42,44,43,48]

# calculating mean and standard deviation of the demand data
mu, sigma = np.mean(vd), np.std(vd)

# function to calculate profit
def calculateNetProfit(D, Q, R, C, S):
    profit = R * min(D, Q) + S * max(0, Q - D) - C * Q
    return profit

# dict to store the average profit for each Q
average_profits = {}

for Q in Qrange:
    # simulate N = 1000 times
    N = 1000
    profits = []

    for _ in range(N):
        # generating a random demand value from a normal distribution
        D = np.random.normal(mu, sigma)
        
        # calculate profit for this iteration
        profit = calculateNetProfit(D, Q, R, C, S)
        profits.append(profit)
    
    # calculate and store the average profit for this Q
    average_profits[Q] = np.mean(profits)

# finding the Q that gives the highest average profit
optimal_Q = max(average_profits, key=average_profits.get)

print(f"The optimal Q is {optimal_Q}, which gives an expected profit of ${average_profits[optimal_Q]:.2f}.")
