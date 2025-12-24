#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            prefix[i + 1] = prefix[i] ^ x
        return [prefix[r + 1] ^ prefix[l] for l, r in queries]
# @lc code=end

