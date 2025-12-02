#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # O(n) solution: dp[i] = maximum amount from first i houses
        # divide from middle
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # steal i-th house or not
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
        """
        # O(n^2) solution: dp[i] = last stolen is the i-th house
        # divide the end
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = nums[i]
            for k in range(i - 1):
                dp[i] = max(dp[k] + nums[i], dp[i])
        return max(dp)
        """
# @lc code=end

