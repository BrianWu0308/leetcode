#
# @lc app=leetcode id=2208 lang=python3
#
# [2208] Minimum Operations to Halve Array Sum
#

# @lc code=start
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        import heapq
        target = sum(nums) / 2.0
        nums = [-float(x) for x in nums]
        heapq.heapify(nums)
        ans = 0
        reduced  = 0
        while reduced < target:
            x = -heapq.heappop(nums)
            half = x / 2.0
            reduced += half
            heapq.heappush(nums, -half)
            ans += 1
        return ans
# @lc code=end

