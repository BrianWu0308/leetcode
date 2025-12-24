#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

# @lc code=start
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from math import comb
        from collections import defaultdict
        ans = comb(len(nums), 2)
        d = defaultdict(int)
        for i, x in enumerate(nums):
            ans -= d[x - i]
            d[x - i] += 1
        return ans

# @lc code=end

