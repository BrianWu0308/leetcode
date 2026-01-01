#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        ans = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, (x * 2 + y))
            ans += 1
        return ans

# @lc code=end

