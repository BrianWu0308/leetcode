#
# @lc app=leetcode id=2815 lang=python3
#
# [2815] Max Pair Sum in an Array
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def max_digit(n: int):
            digit = 0
            while n > 0:
                digit = max(n % 10, digit)
                n //= 10
            return digit
        d = {}
        ans = -1
        for x in nums:
            key = max_digit(x)
            if key in d:
                ans = max(ans, x + d[key])
                d[key] = max(d[key], x)
            else:
                d[key] = x
        return ans
# @lc code=end

