#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        import math
        nums = [-x for x in nums]
        heapq.heapify(nums)
        ans = 0
        for _ in range(k):
            x = -heapq.heappop(nums)
            ans += x
            x = math.ceil(x / 3)
            heapq.heappush(nums, -x)
        return ans
# @lc code=end

