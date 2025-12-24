#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # ai + aj == 0
        ans = -1
        seen = set()
        for x in nums:
            if -x in seen:
                ans = max(abs(x), ans)
            else:
                seen.add(x)
        return ans

# @lc code=end

