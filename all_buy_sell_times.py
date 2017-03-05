#list all times when you should buy stock and when you should sell stock
stock_prices = [5,4,2,5,7,7,3,2,1,0]

def optimal_buy_sell_times(stock_prices):
    descending_stock_prices = sorted(stock_prices,reverse=True)
    descending_idx = 0

    temp_buy_idxs = []
    buy_idxs = []
    sell_idxs = []

    for idx, elem in enumerate(stock_prices):
        if elem != descending_stock_prices[descending_idx]:
            temp_buy_idxs.append(idx)
        elif elem == descending_stock_prices[descending_idx]:
            if len(sell_idxs) == 0:
                sell_idxs.append(idx)
                descending_idx += 1
                buy_idxs.extend(temp_buy_idxs)
                temp_buy_idxs = []
            elif len(buy_idxs) > 0:
                if sell_idxs[-1] < buy_idxs[-1]:
                    sell_idxs.append(idx)
                    descending_idx += 1
                    buy_idxs.extend(temp_buy_idxs)
                    temp_buy_idxs = []

    print buy_idxs
    print sell_idxs




print stock_prices
print optimal_buy_sell_times(stock_prices)
