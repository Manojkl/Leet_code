class Solution:
    def maxProfit(self, prices):
        best_profit = 0
        m = 1
        day = None
        if len(prices) == 2:
            if prices[1] > prices[0]:
                best_profit = prices[1] - prices[0]
            else:
                best_profit = 0
            return best_profit
        while m<len(prices):
            for i in prices[m:]:
                profit = i - prices[m-1]
                if profit > best_profit:
                    best_profit = profit
            m+=1
        print(best_profit)
        return best_profit

profit = Solution()
List = [7,1,5,3,6,4]
profit.maxProfit(List)