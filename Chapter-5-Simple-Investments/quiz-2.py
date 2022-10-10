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
        