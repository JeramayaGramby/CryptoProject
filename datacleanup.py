"""Importing all necessary modules"""
import pandas as pd
from pathlib import Path

'''Drop all tables except for close through sorting'''
'''Merge all tables into their respective data sets'''

'''Stablecoin Data'''

DAI = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'DAI-USD.csv'
DGD = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'DGD-USD.csv'
GUSD = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'GUSD-USD.csv'
SBD = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'SBD-USD.csv'
SHX = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'SHX-USD.csv'
SUSD = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'SUSD-USD.csv'
TUSD = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'TUSD-USD.csv'
USDC = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'USDC-USD.csv'
USDP = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'USDP-USD.csv'
USDT = Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'USDT-USD.csv'

'''S&P 500 Data'''
AAPL = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'AAPL.csv'
AMZN = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'AMZN.csv'
BRKB = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'BRK-B.csv'
GOOG = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'GOOG.csv'
GOOGL = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'GOOGL.csv'
META = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'META.csv'
MSFT = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'MSFT.csv'
NVDA = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'NVDA.csv'
TSLA = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'TSLA.csv'
UNH = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'UNH.csv'

SP_500_List = list([AAPL,AMZN,BRKB,GOOG,GOOGL,META,MSFT,NVDA,TSLA,UNH])
for item in SP_500_List:
    result = pd.read_csv(item)
    print(result)

stablecoin_List = list([DAI,DGD,GUSD,SBD,SHX,SUSD,TUSD,USDC,USDP,USDT])
for item in stablecoin_List:
    result = pd.read_csv(item)
    print(result)

'''SP_500_Top_10_Data = pd.concat(map(pd.read_csv, 'AAPL','AMZN','BRKB','GOOG','GOOGL','META','MSFT','NVDA','TSLA','UNH'))
print(SP_500_Top_10_Data)'''
'''Stablecoin_Historical_Data = pd.concat(map(pd.read_csv, DAI,DGD,GUSD,SBD,SHX,SUSD,
TUSD,USDC,USDP,USDT))'''


'''

DAI_Data = pd.read_csv(DAI)
DAI_Data.info()
'''

'''
DGD_Data = pd.read_csv(DGD)
GUSD_Data = pd.read_csv(GUSD)
SBD_Data = pd.read_csv(SBD)
SHX_Data = pd.read_csv(SHX)
SUSD_Data =pd.read_csv(SUSD)
TUSD_Data = pd.read_csv(TUSD)
USDC_Data = pd.read_csv(USDC)
USDP_Data = pd.read_csv(USDP)
USDT_Data = pd.read_csv(USDT)
'''

AMZN = Path.home() / 'CryptoAnalysis' / 'SP_500_Top_10_Data' / 'AMZN.csv'
AMZN_Data = pd.read_csv(AMZN)
print(AMZN_Data)
'''AAPL_Data = pd.read_csv(AAPL)
BRKB_Data = pd.read_csv(BRKC)
print(AAPL_Data)
print(BRKB_Data)'''

'''AMZN_Data = pd.read_csv(AMZN)
BRKB_Data = pd.read_csv(BRKB)
GOOG_Data = pd.read_csv(GOOG)
GOOGL_Data =pd.read_csv(GOOGL)
META_Data = pd.read_csv(META)
MSFT_Data = pd.read_csv(MSFT)
NVDA_Data = pd.read_csv(NVDA)
UNH_Data = pd.read_csv(UNH)
'''



'''for x in list(DAI_Data,DGD_Data,SBD_Data,SHX_Data,SUSD_Data,TUSD_Data,USDC_Data,USDP_Data,USDT_Data):
    print(x.info())'''


