#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digits_sum(n: int):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        d = {}
        ans = -1
        for x in nums:
            s = digits_sum(x)
            if s in d:
                ans = max(x + d[s], ans)
                d[s] = max(x, d[s])
            else:
                d[s] = x
        return ans
# @lc code=end

