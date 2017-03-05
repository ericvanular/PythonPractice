# Given an array with successive stock prices, give an O(n) 
#algorithm that finds the idea single buy/sell indices. 

def find_ideal_single_buy_sell(stock_vals):
    max_diff = float("-inf")
    min_val = stock_vals[0]

    for idx in range(1, len(stock_vals)):
        curr_diff = stock_vals[idx] - min_val
        if curr_diff > max_diff:
            max_diff = curr_diff
        if stock_vals[idx] < min_val:
            min_val = stock_vals[idx]
    return max_diff


stock_prices = [5,3,7,0]
print find_ideal_single_buy_sell(stock_prices)