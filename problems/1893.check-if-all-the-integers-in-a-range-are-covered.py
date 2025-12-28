#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        from itertools import accumulate
        d = [0] * 52
        for start, end in ranges:
            d[start] += 1
            d[end + 1] -= 1
        a = list(accumulate(d))
        return all(a[i] >= 1 for i in range(left, right + 1))
# @lc code=end

