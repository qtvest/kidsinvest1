def single_profit_or_loss(money_spent, buy_price, sell_price):
    shares = money_spent / buy_price
    profit_or_loss = shares * (sell_price - buy_price)
    return profit_or_loss

def single_asset_invest_PnL(price_data, money_spent, buy_date, sell_date):
    buy_price = price_data[buy_date]
    sell_price = price_data[sell_date]
    return single_profit_or_loss(money_spent, buy_price, sell_price)
        
def equal_split_assets_invest_PnL(all_price_data, asset_tickers, total_money_spent, buy_date, sell_date):
    number_of_assets = len(asset_tickers)
    money_spent_each_asset = total_money_spent / number_of_assets
    total_profit = 0
    for ticker in asset_tickers:
        price_data = all_price_data[ticker]
        asset_profit = single_asset_invest_PnL(price_data, money_spent_each_asset, buy_date, sell_date)
        total_profit = total_profit + asset_profit        
    return total_profit
    
def split_assets_invest_PnL(all_price_data, asset_splits, total_money_spent, buy_date, sell_date):
    sum_of_split = 0
    for asset,split in asset_splits.items():
        if split < 0:
            raise Exception("Asset {} has a negative split {}".format(asset, split))
        sum_of_split += split
    if sum_of_split != 1.0:
        raise Exception("The sum of asset splits must be equal to 1.0")
        
    total_profit = 0
    for asset,split in asset_splits.items():
        price_data = all_price_data[asset]
        money_spent_on_asset = total_money_spent * split
        asset_profit = single_asset_invest_PnL(price_data, money_spent_on_asset, buy_date, sell_date)
        total_profit = total_profit + asset_profit        
    return total_profit
        
