#
# @lc app=leetcode id=3275 lang=python3
#
# [3275] K-th Nearest Obstacle Queries
#

# @lc code=start
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        import heapq
        h = []
        heapq.heapify(h)
        ans = []
        for x, y in queries:
            heapq.heappush(h, -(abs(x) + abs(y)))
            if len(h) > k:
                heapq.heappop(h)
            ans.append(-1 if len(h) < k else -h[0])
        return ans
            

# @lc code=end

