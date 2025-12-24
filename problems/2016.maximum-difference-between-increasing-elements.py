#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = float('inf')
        ans = 0
        for x in nums:
            min_val = min(x, min_val)
            ans = max(x - min_val, ans)
        if ans == 0:
            return -1
        return ans
# @lc code=end

