#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        r_acc = 1
        for i in range(len(nums) - 2, -1, -1):
            r_acc *= nums[i + 1]
            answer[i] *= r_acc
        return answer

# @lc code=end

