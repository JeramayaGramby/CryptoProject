"""Importing all necessary modules"""
import pandas as pd
from pathlib import Path

'''Stablecoin'''
'''
DAI = pathlib.Path('DGD-USD.csv')
DGD = pathlib.Path('DGD-USD.csv')
GUSD = pathlib.Path('GUSD-USD.csv')
SBD = pathlib.Path('SBD-USD.csv')
SHX = pathlib.Path('SHX-USD.csv')
SUSD = pathlib.Path('SUSD-USD.csv')
TUSD = pathlib.Path('TUSD-USD.csv')
USDC = pathlib.Path('USDC-USD.csv')
USDP = pathlib.Path('USDP-USD.csv')
USDT = pathlib.Path('USDT-USD.csv')
'''

'''S&P 500 Data'''
AAPL = Path('AAPL.csv')

'''AMZN = pathlib.Path('AMZN.csv')
BRKB = pathlib.Path('BRK-B.csv')
GOOG = pathlib.Path('GOOG.csv')
GOOGL = pathlib.Path('GOOGL.csv')
META = pathlib.Path('META.csv')
MSFT = pathlib.Path('MSFT.csv')
NVDA = pathlib.Path('NVDA.csv')
TSLA = pathlib.Path('TSLA.csv')
UNH = pathlib.Path('UNH.csv')
'''

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

AAPL_Data = pd.read_csv(AAPL)

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


