#
# @lc app=leetcode id=2001 lang=python3
#
# [2001] Number of Pairs of Interchangeable Rectangles
#

# @lc code=start
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = {}
        ans = 0
        for w, h in rectangles:
            ratio = w / h
            if ratio in d:
                ans += d[ratio]
                d[ratio] += 1
            else:
                d[ratio] = 1
        return ans

# @lc code=end

