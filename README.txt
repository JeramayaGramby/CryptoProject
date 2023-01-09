This README file contains the purpose of this project, weaknesses of the project and instructions for using the program. 

Project Purpose:

The purpose of this project is to compare the performance of a 'stablecoin' portfolio consisting of the most liquid 'stablecoin' blockchain
assets to the performance of the highest weighted companies in the S&P 500 by performing Sharpe Ratio analysis which accounts for risk when
calculating projected returns. 

Stablecoin blockchain assets are cryptocurrencies that are backed by physical assets or fiat currency.
The S&P 500 is a stock index that tracks the performance of the 500 largest companies trading on the NASDAQ and NYSE. 

This project utilizes the 10 highest weighted companies on the S&P 500 and the 10 most liquid stablecoin assets. The 10 highest weighted 
companies have the highest impact on the S&P 500 index's price and therefore are assumed to be the most stable companies in the S&P 500 index
excluding volatility ratio and dividend return analysis. 

Liquidity, measured in 24 hour trading volume and market capitalization, is preferred for stablecoin assets in this project because high 
liquidity assumes the highest demand and financial support from the community when compared to its peers. However, several coins that made 
the top 10 were not considered for the project because these assets does not possess the project's imposed requirement of 4 years worth of 
historical data.  

Weaknesses:

This project has a many shortcomings. First off, the pyportfolioopt module DOES NOT support Python 3.11 as of January 8, 2023 so 3.7-3.10 must
be the configured interpreter. In terms of the data collection process, liquid stablecoins with at least 4 years of historical data 
are difficult to find so the conclusions drawn from the data made on January 8, 2023 could look drastically different over time. 

Several different APIs, including Yahoo Finance's API, did not properly query all the requested stablecoin data. 
For DAI-USD, data recorded on and before November 22, 2019 on Yahoo Finance was missing and Coincodex was missing data for DAI-USD
recorded on January 30, 2019. Data inaccuracy made the data collection process unneccessarily more difficult.

Volatility ratio analysis and dividend returns were not considered in the S&P 500 index portfolio. 
Both volatility and dividend returns influence total returns and could have impacted the assets analyzed for the project. 
Considering dividend returns for most companies on the S&P 500 will not dramatically alter the portfolio's returns because most companies on 
the S&P 500 index do not have very significant dividends. However if volatility was a factor in the portfolio construction then TSLA would 
not be in the portfolio because TSLA was the only company possessing a beta of 2 or above.

Instructions:

1. Ensure all dependencies are installed correctly and Python 3.7, 3.8, 3.9 or 3.10 is the interpreter.
2. If PyPortfolioOpt is not installed use "py -3.10 -m pip install PyPortfolioOpt --use-pep517". Install Cmake and pulp if necessary.
3. Run main.py