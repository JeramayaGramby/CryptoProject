"""Importing all necessary modules"""
import pandas as pd
import numpy as np
import cmake
from pypfoft.efficienct_frontier import EfficientFrontier
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

