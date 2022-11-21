# problem : given a stock prices of each day, choose the maximum profit if you can only buy in 1 of the days
#           adn the sell in the later day

# def maxProfit(prices: int) -> int:
#     minPrice = []
#     maxProfit = 0
#     for i in range(len(prices)):
#         if i == 0:
#             minPrice.append(prices[0])
#         else:
#             if(prices[i] < minPrice[i-1]):
#                 minPrice.append(prices[i])
#             else:
#                 minPrice.append(minPrice[i-1])
        
#         if(prices[i] - minPrice[i] > maxProfit):
#             maxProfit = prices[i] - minPrice[i]
    
#     return maxProfit

def maxProfit(prices: int) -> int:
    lastMinPrice = prices[0]
    maxProfit = 0
    for i in range(len(prices)):
        if(prices[i] < lastMinPrice):
            lastMinPrice = prices[i]
        
        if(prices[i] - lastMinPrice > maxProfit):
            maxProfit = prices[i] - lastMinPrice
    
    return maxProfit