# Function definition
def max_profit(stock_prices):
	
	#check if at least two prices are there
	if len(stock_prices) < 2:
		raise IndexError('At least two prices needed')

	#initialize the min price and max profit
	#note that byuing price minimum and selling price
	#maximum gives best profit
	min_price = stock_prices[0]
	max_profit = stock_prices[1] - stock_prices[0] #first need to buy

	for idx, current_price in enumerate(stock_prices):

		#we can not sell first, hence skip the first index
		if idx == 0:
			continue

		#see the profit if we buy at min_price
		#and sell at current price
		potential_profit = current_price - min_price

		#update max_profit
		max_profit = max(max_profit, potential_profit)

		#update min_price, so it is always the lowest 
		#price we have seen so far
		min_price = min(min_price, current_price)
	return max_profit

#test
stock_prices = [10,7,5,8,11,9]
print max_profit(stock_prices)
