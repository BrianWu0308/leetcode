#
# @lc app=leetcode id=2848 lang=python3
#
# [2848] Points That Intersect With Cars
#

# @lc code=start
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        from itertools import accumulate
        d = [0] * 102
        for start, end in nums:
            d[start] += 1
            d[end + 1] -= 1
        return sum(x >= 1 for x in accumulate(d))
# @lc code=end

