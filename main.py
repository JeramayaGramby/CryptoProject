"""Importing all necessary modules"""
import pandas as pd
from pathlib import Path
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns



stablecoin_data = pd.read_csv(Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'Stablecoin_Agg_Data.csv').drop(columns="index")
sp_500_data = pd.read_csv(Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'SP_500_Agg_Data.csv').drop(columns="index")

print(stablecoin_data)
print(sp_500_data)

'''Preparing the machine learning model'''

mu1 = expected_returns.mean_historical_return(prices=stablecoin_data,returns_data=False,compounding=True)
mu2 = expected_returns.mean_historical_return(prices=stablecoin_data,returns_data=False,compounding=True)

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