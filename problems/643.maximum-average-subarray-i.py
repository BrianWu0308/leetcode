#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float('-inf')
        sum = 0.0
        for i, num in enumerate(nums):
            sum += num
            left = i - k + 1
            if left < 0:
                continue
            ans = max(ans, sum)
            sum -= nums[left]
        return ans / k

# @lc code=end

