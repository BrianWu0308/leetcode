#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, item in enumerate(nums):
            if item in target_dict:
                return [target_dict[item], i]
            else:
                target_dict[target - item] = i


# @lc code=end

