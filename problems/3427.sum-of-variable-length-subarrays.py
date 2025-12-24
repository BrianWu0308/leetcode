#
# @lc app=leetcode id=3427 lang=python3
#
# [3427] Sum of Variable Length Subarrays
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        ans = 0
        for i in range(n):
            start = max(0, i - nums[i])
            ans += prefix[i + 1] - prefix[start]
        return ans

# @lc code=end

