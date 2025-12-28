#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#

# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        from itertools import accumulate
        d = [0] * 2051
        for birth, death in logs:
            d[birth] += 1
            d[death] -= 1
        a = list(accumulate(d))
        return max(range(len(a)), key=lambda i: a[i])
# @lc code=end

