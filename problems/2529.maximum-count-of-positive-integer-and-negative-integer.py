#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        def lower_bound(target):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        neg_count = lower_bound(0)
        pos_count = n - lower_bound(1)
        return max(neg_count, pos_count)
# @lc code=end

