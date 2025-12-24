#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        ans = float('inf')
        for i, x in enumerate(cards):
            if x in d:
                ans = min(i - d[x] + 1, ans)
            d[x] = i
        return ans if ans != float('inf') else -1
# @lc code=end

