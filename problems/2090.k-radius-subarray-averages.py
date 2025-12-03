#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        ans = [-1] * n
        if window_size > n:
            return ans
        if k == 0:
            return nums
        cur_sum = sum(nums[:k])
        for i in range(n):
            r = i + k
            l = i - k
            if r < n:
                cur_sum += nums[r]
            if l < 0 or r >= n:
                continue
            else:
                ans[i] = cur_sum // window_size
                cur_sum -= nums[l]
        return ans

# @lc code=end

