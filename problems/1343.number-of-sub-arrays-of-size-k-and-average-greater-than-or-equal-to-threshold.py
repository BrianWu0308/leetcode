#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = 0
        ans = 0
        threshold *= k
        for i, num in enumerate(arr):
            cur_sum += num
            left = i - k + 1
            if left < 0:
                continue
            if cur_sum >= threshold:
                ans += 1
            cur_sum -= arr[left]
        return ans

# @lc code=end

