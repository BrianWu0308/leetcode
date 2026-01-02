#
# @lc app=leetcode id=2233 lang=python3
#
# [2233] Maximum Product After K Increments
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums) + 1)
        ans = 1
        MOD = 1_000_000_007
        for x in nums:
            ans *= x
        return ans % MOD
# @lc code=end

