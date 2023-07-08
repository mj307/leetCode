'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
'''

# this first part creates a list of the days the stocks rise and by how much they increase
prices = [6,1,3,2,4,7]
print (prices)
profit_list = []
total_profit = 0 # total profit made
for buyingDay in range(0,len(prices)-1):
    sellingDay = buyingDay+1
    if 0 < prices[sellingDay] - prices[buyingDay]:
        profit_list.append([prices[sellingDay] - prices[buyingDay], buyingDay, sellingDay])

# this second part arranges the list in order of potential buying days
from operator import itemgetter
profit_list = sorted(profit_list, key=itemgetter(1))
print (profit_list)
# this third part sees which combination of days will yield the highest profits
max_profit = 0
for profit in range(0, len(profit_list)):
    print ("NEW: "+ str(profit_list[profit]))
    total_profit = profit_list[profit][0]
    sellingDay = profit_list[profit][2]
    buyingDay = profit_list[profit][1]
    for each in range(profit+1, len(profit_list)):
        if profit_list[each][1] >= sellingDay:
            print ("HERE "+str(profit_list[each]))
            total_profit += profit_list[each][0]
            sellingDay = profit_list[each][2]
    if max_profit < total_profit:
        max_profit = total_profit
    print (max_profit)
print (max_profit)

