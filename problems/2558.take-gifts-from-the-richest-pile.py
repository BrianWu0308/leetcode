#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        import math
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            mx = -heapq.heappop(gifts)
            mx = math.isqrt(mx)
            heapq.heappush(gifts, -mx)
        return -1 * sum(gifts)
# @lc code=end

