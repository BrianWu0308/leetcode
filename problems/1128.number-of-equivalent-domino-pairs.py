#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        ans = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            if key in freq:
                ans += freq[key]
                freq[key] += 1
            else:
                freq[key] = 1
        return ans
# @lc code=end