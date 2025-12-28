#
# @lc app=leetcode id=3652 lang=python3
#
# [3652] Best Time to Buy and Sell Stock using Strategy
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        ps = [p * s for p, s in zip(prices, strategy)]
        pps = [0] * (n + 1)
        sumSell = [0] * (n + 1)

        for i, x in enumerate(ps):
            pps[i + 1] = pps[i] + x

        for i, x in enumerate(prices):
            sumSell[i + 1] = sumSell[i] + x

        ans = float('-inf')
        for i in range(k, n + 1):
            profit = sumSell[i] - sumSell[i - (k // 2)] + pps[n] - pps[i] + pps[i - k]
            ans = max(profit, ans)
            
        return max(pps[n], ans)
        

# @lc code=end

