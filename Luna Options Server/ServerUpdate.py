"""
Script for server updates, can change based on needs
"""
import APICallScript as api
import LunaOptionsDB as db
import SandP500List as snp

def update():
    luna = db.LunaDB()
    api_obj = api.APICalls()
    for ticker in snp.ticker_list:
        luna.add_column(ticker, '_options', 'historicalVolatility', 'varchar(32)')

        hv = api_obj.historical_volatility_call(ticker)
        historical_volatility = hv['indicator'][0][0]
        historical_volatility = float(historical_volatility)
        historical_volatility = round(historical_volatility, 4)
        historical_volatility = historical_volatility * 100
        luna.update_column_conditional(ticker, '_options', 'historicalVolatility', historical_volatility, 'id', '1')

    print('Update Complete!')

update()

