"""Importing all necessary modules"""
import pandas as pd
from pathlib import Path

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
AAPL = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'AAPL.csv'
AMZN = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'AMZN.csv'
BRKB = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'BRK-B.csv'
GOOG = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'GOOG.csv'
GOOGL = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'GOOGL.csv'
META = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'META.csv'
MSFT = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'MSFT.csv'
NVDA = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'NVDA.csv'
TSLA = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'TSLA.csv'
UNH = Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'UNH.csv'

SP_500_List = list([AAPL,AMZN,BRKB,GOOG,GOOGL,META,MSFT,NVDA,TSLA,UNH])
Stablecoin_List = list([DAI,DGD,GUSD,SBD,SHX,SUSD,TUSD,USDC,USDP,USDT])

'''Left Joining each CSV file by asset type and converting the dataframes to annualized daily simple returns'''
class data_processor:
    def SP_500():
        AAPL_Table = pd.read_csv(AAPL).loc[:, ["Date","AAPL"]]
        AMZN_Table = pd.read_csv(AMZN).loc[:, ["Date","AMZN"]]
        BRKB_Table = pd.read_csv(BRKB).loc[:, ["Date","BRKB"]]
        GOOG_Table = pd.read_csv(GOOG).loc[:, ["Date","GOOG"]]
        GOOGL_Table = pd.read_csv(GOOGL).loc[:, ["Date","GOOGL"]]
        META_Table = pd.read_csv(META).loc[:, ["Date","META"]]
        MSFT_Table = pd.read_csv(MSFT).loc[:, ["Date","MSFT"]]
        NVDA_Table = pd.read_csv(NVDA).loc[:, ["Date","NVDA"]]
        TSLA_Table = pd.read_csv(TSLA).loc[:, ["Date","TSLA"]]
        UNH_Table = pd.read_csv(UNH).loc[:, ["Date","UNH"]]

        Merged_Table = AAPL_Table.merge(AMZN_Table, on='Date', how='left').merge(BRKB_Table, on='Date', how='left').merge(
            GOOG_Table, on='Date', how='left').merge(GOOGL_Table, on='Date', how='left').merge(META_Table, on='Date', how='left').merge(
                MSFT_Table, on='Date', how='left').merge(NVDA_Table, on='Date', how='left').merge(
                    TSLA_Table, on='Date', how='left').merge(UNH_Table, on='Date', 
                    how='left').set_index('Date')
        
        Daily_Returns = Merged_Table.pct_change(periods=1).mean()
        Annualized_Returns = Daily_Returns.mul(other=252*100)

        Annualized_Returns.to_csv(Path.home() / 'CryptoAnalysis' / 'SP_500_Historical_Data' / 'SP_500_Agg_Data.csv')    

    def Stablecoin():
        DAI_Table = pd.read_csv(DAI).loc[:, ["Date","DAI"]]
        DGD_Table = pd.read_csv(DGD).loc[:, ["Date","DGD"]]
        GUSD_Table = pd.read_csv(GUSD).loc[:, ["Date","GUSD"]]
        SBD_Table = pd.read_csv(SBD).loc[:, ["Date","SBD"]]
        SHX_Table = pd.read_csv(SHX).loc[:, ["Date","SHX"]]
        SUSD_Table = pd.read_csv(SUSD).loc[:, ["Date","SUSD"]]
        TUSD_Table = pd.read_csv(TUSD).loc[:, ["Date","TUSD"]]
        USDC_Table = pd.read_csv(USDC).loc[:, ["Date","USDC"]]
        USDP_Table = pd.read_csv(USDP).loc[:, ["Date","USDP"]]
        USDT_Table = pd.read_csv(USDT).loc[:, ["Date","USDT"]]

        Merged_Table = DAI_Table.merge(DGD_Table, on='Date', how='left').merge(GUSD_Table, on='Date', how='left').merge(
            SBD_Table, on='Date', how='left').merge(SHX_Table, on='Date', how='left').merge(SUSD_Table, on='Date', how='left').merge(
                TUSD_Table, on='Date', how='left').merge(USDC_Table, on='Date', how='left').merge(
                    USDP_Table, on='Date', how='left').merge(USDT_Table, on='Date', 
                    how='left').set_index('Date')
        
        Daily_Returns = Merged_Table.pct_change(periods=1).mean()
        Annualized_Returns = Daily_Returns.mul(other=252*100)

        Annualized_Returns.to_csv(Path.home() / 'CryptoAnalysis' / 'Stablecoin_Historical_Data' / 'Stablecoin_Agg_Data.csv')


data_processor.SP_500()
data_processor.Stablecoin()





