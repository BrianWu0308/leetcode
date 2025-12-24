#
# @lc app=leetcode id=3623 lang=python3
#
# [3623] Count Number of Trapezoids I
#

# @lc code=start
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import Counter
        MOD = 1_000_000_007
        cnt = Counter(p[1] for p in points)
        ans = 0
        previous_edges = 0
        for c in cnt.values():
            current_edges = c * (c - 1) // 2
            ans += current_edges * previous_edges
            previous_edges += current_edges
        return ans % MOD
                
# @lc code=end

