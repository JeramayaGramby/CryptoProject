This README file contains the purpose of this project, weaknesses of the project and instructions for using the program. 

Project Purpose:

The purpose of this project is to compare the performance of a 'stablecoin' portfolio consisting of the most liquid 'stablecoin' blockchain
assets to the performance of the highest weighted companies in the S&P 500 by performing Sharpe Ratio analysis. 

Stablecoin blockhain assets are cryptocurrencies that are backed by physical assets or fiat currency and the S&P 500 is a stock index 
that tracks the performance of the 500 largest companies trading on the NASDAQ and NYSE. 

This project utilizes the 10 highest weighted companies on the S&P 500 and the 10 most liquid stablecoin assets. The 10 highest weighted 
companies have the highest impact on the S&P 500 index's price and therefore are assumed to be the most stable companies in the S&P 500 index
excluding volatility ratio and dividend return analysis. 

Liquidity, measured in 24 hour trading volume and market capitalization, is preferred for stablecoin assets in this project because high 
liquidity assumes the highest demand and financial support from the community when compared to its peers. However, several coins that made 
the top 10 were not considered for the project because these assets does not possess the project's imposed requirement of 4 years worth of 
historical data.  

Weaknesses:

This project has a few shortcomings. Many stablecoins do not have extensive historical data so the predictions made in this model
may look very different in a year or two from 1/8/2023. Volatility ratio analysis was not conducted on the ten companies in the S&P 500 index
portfolio and dividend returns for the 10 selected companies were also not considered. Both volatility and dividend returns influence total 
returns and could have impacted the assets analyzed for the project. Considering dividend returns for most companies on the S&P 500 will not
dramatically alter the portfolio's returns because most companies on the S&P 500 index do not have very significant dividends. However if 
volatility was a factor for the portfolio construction then TSLA would not be in the portfolio because TSLA was the only company possessing a 
beta of 2 or above.

Instructions:

1. Ensure all dependencies are installed correctly and properly configured.
2. Run main.py