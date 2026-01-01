#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq, math
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for _ in range(k):
            x = -heapq.heappop(piles)
            x -= math.floor(x / 2)
            heapq.heappush(piles, -x)
        return -1 * sum(piles)
# @lc code=end

