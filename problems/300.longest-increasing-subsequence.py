#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        # dp[i]: the sequence length end with nums[i]
        for i in range(1, n):
            for k in range(i):
                if nums[k] < nums[i]:
                    dp[i] = max(dp[i], dp[k] + 1)
        return max(dp)

# @lc code=end

