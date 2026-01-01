#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        from itertools import accumulate
        d = [0] * (len(nums) + 1)
        for l, r in queries:
            d[l] += 1
            d[r + 1] -= 1
        a = list(accumulate(d))[:-1]
        return all(a[i] >= nums[i] for i in range(len(nums)))
# @lc code=end

