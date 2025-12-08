#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        distinct = 0
        cur_sum = 0
        max_sum = 0
        for i, x in enumerate(nums):
            cur_sum += x
            freq[x] += 1
            if freq[x] == 1:
                distinct += 1
            l = i - k + 1
            if l < 0:
                continue
            if distinct == k:
                max_sum = max(cur_sum, max_sum)
            cur_sum -= nums[l]
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                distinct -= 1
        return max_sum
# @lc code=end

