"""Importing all necessary modules"""
import pandas as pd
import numpy as np
import cmake
import pulp
from pypfoft.efficienct_frontier import EfficientFrontier
from pypfopt.discrete_allocation import DiscreteAllocation
from pypfoft import risk_models
from pypfoft import expected_returns

stablecoin_data = pd.read_csv('')
sp_500_data = pd.read_csv('')

stablecoin_data.dropna(inplace=True, axis = 1)
sp_500_data.dropna(inplace=True, axis = 1)

stablecoin_daily_returns = stablecoin_data.pct_change(1)
sp_500_daily_returns = sp_500_data.pct_change(1)
print(stablecoin_daily_returns)
print(sp_500_daily_returns)

stablecoin_avg_daily_returns = stablecoin_daily_returns.mean()
sp_500_avg_daily_returns = stablecoin_daily_returns.mean()
print(stablecoin_avg_daily_returns)
print(sp_500_avg_daily_returns)

print(stablecoin_avg_daily_returns * 252)
print(sp_500_avg_daily_returns * 252)

sp_500_avg_daily_returns.sort_values(axis=0, ascending = False, kind = 'quicksort', na_position='last', ignore_index ='False', key=None)
stablecoin_avg_daily_returns.sort_values(axis=0, ascending = False, kind = 'quicksort', na_position='last', ignore_index ='False', key=None)

print(stablecoin_avg_daily_returns * 252 * 100)
print(sp_500_avg_daily_returns * 252 * 100)

'''Preparing the machine learning model'''
mu1 = expected_returns.mean_historical_return(stablecoin_data)
mu2 = expected_returns.mean_historical_return(stablecoin_data)
S1 = risk_models.sample_cov(stablecoin_data)
S2 = risk_models.sample_cov(sp_500_data)
'''Sharpe Ratio Optimization'''
ef1 = EfficientFrontier(mu1,S1)
ef2 = EfficientFrontier(mu2,S2)
stablecoin_weights = ef1.max_sharpe()
sp_500_weights = ef2.max_sharpe()
stablecoin_cleaned_weights = ef1.clean_weights
sp_500_cleaned_weights = ef2.clean_weights
stablecoin_performance = ef1.portfolio_performance(verbose = True)
sp_500_performance = ef2.portfolio_performance(verbose = True)
print(stablecoin_performance)
print(sp_500_performance)
print(stablecoin_cleaned_weights)
print(sp_500_cleaned_weights)

'''Calculating optimal portfolio weights for each asset'''
stablecoin_portfolio_value = 10000
sp_500_portfolio_value = 10000
stablecoin_latest_prices = stablecoin_data.tail(1).squeeze()
sp_500_latest_prices = sp_500_data.tail(1).squeeze()
da1 = DiscreteAllocation(stablecoin_weights, stablecoin_latest_prices, total_portfolio_value = stablecoin_portfolio_value)
da2 = DiscreteAllocation(sp_500_weights, sp_500_latest_prices, total_portfolio_value = sp_500_portfolio_value)

stablecoin_allocation, stablecoin_leftover = da1.lp_portfolio()
sp_500_allocation, sp_500_leftover = da2.lp_portfolio
print('Stablecoin Allocation:', stablecoin_allocation)
print('Remaining Capital:', stablecoin_leftover)
print('S&P 500 Stock Allocation:', sp_500_allocation)
print('Remaining Capital:', sp_500_leftover)

'''Obtaining Discrete Allocation Values'''
stablecoin_discrete_allocation_list = []
sp_500_discrete_allocation_list = []

for symbol in stablecoin_allocation:
    stablecoin_discrete_allocation_list.append(sp_500_allocation.get(symbol))

for symbol in sp_500_allocation:
    sp_500_discrete_allocation_list.append(sp_500_allocation.get(symbol))


'''Creating Shape Ratio Optimized tabular dataframes'''
sharpe_stablecoin_portfolio = pd.DataFrame(columns= ['Coin_Ticker', 'Discrete_Value'+str(stablecoin_portfolio_value)])
sharpe_stablecoin_portfolio['Coin_Ticker'] = stablecoin_allocation
sharpe_stablecoin_portfolio['Discrete_Value'+str(stablecoin_portfolio_value)] = stablecoin_discrete_allocation_list
sharpe_stablecoin_portfolio['Price'] = stablecoin_latest_prices[stablecoin_allocation]
print(sharpe_stablecoin_portfolio)

sharpe_sp_500_portfolio = pd.DataFrame(columns= ['Coin_Ticker', 'Discrete_Value'+str(sp_500_portfolio_value)])
sharpe_sp_500_portfolio['Company_Ticker'] = sp_500_allocation
sharpe_sp_500_portfolio['Discrete_Value'+str(sp_500_portfolio_value)] = sp_500_discrete_allocation_list
sharpe_sp_500_portfolio['Price'] = sp_500_latest_prices[sp_500_allocation]
print(sharpe_sp_500_portfolio)