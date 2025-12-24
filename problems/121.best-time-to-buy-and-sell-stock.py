#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        ans = 0
        for x in prices:
            min_price = min(x, min_price)
            ans = max(x - min_price, ans)
        return ans
# @lc code=end

