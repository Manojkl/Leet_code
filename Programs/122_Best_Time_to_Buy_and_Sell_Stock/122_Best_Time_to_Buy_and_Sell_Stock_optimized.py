class Solution:
    def maxProfit(self, prices):

        if len(prices) == 1:
            return 0
        least_value = prices[0]
        best_profit = float('-inf')
        for k in range(1,len(prices)):
            best_profit = max(best_profit, prices[k]-least_value)

            if least_value > prices[k]:
                least_value = prices[k]
        print(best_profit)
        if best_profit <=0:
            return 0
        return best_profit

profit = Solution()
List = [7,1,5,3,6,4]
profit.maxProfit(List)