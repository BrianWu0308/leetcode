#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        return max(prefix) - min(prefix)
# @lc code=end

