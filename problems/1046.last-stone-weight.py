#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(x - y))
        if stones:
            return -heapq.heappop(stones)
        return 0

# @lc code=end

