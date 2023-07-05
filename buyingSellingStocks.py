'''
PROBLEM STATEMENT:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

prices = [7,1,5,3,6,4]

max = 0 # biggest difference in value between buying and selling
for buyingDayPrice in range(0,len(prices)):
    for sellingDayPrice in range(buyingDayPrice+1,len(prices)):
        if max < sellingDayPrice - buyingDayPrice:
            max = sellingDayPrice - buyingDayPrice
print (max)
