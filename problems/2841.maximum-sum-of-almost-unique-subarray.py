#
# @lc app=leetcode id=2841 lang=python3
#
# [2841] Maximum Sum of Almost Unique Subarray
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        distinct = 0
        cur_sum = 0
        ans = 0
        for i, num in enumerate(nums):
            cur_sum += num
            freq[num] += 1
            if freq[num] == 1:
                distinct += 1
            l = i - k + 1
            if l < 0:
                continue
            if distinct >= m:
                ans = max(cur_sum, ans)
            cur_sum -= nums[l]
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                distinct -= 1
        return ans

# @lc code=end

