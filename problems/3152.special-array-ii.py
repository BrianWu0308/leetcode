#
# @lc app=leetcode id=3152 lang=python3
#
# [3152] Special Array II
#

# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0] * len(nums)
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        return [prefix[r] - prefix[l] == 0 for l, r in queries]
# @lc code=end

