#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from itertools import accumulate
        d = [0] * 1001
        for n, start, end in trips:
            d[start] += n
            d[end] -= n
        return all(a <= capacity for a in accumulate(d))
# @lc code=end

