#
# @lc app=leetcode id=3412 lang=python3
#
# [3412] Find Mirror Score of a String
#

# @lc code=start
class Solution:
    def calculateScore(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        ans = 0
        mapping = {chr(ord('a') + i): chr(ord('z') - i) for i in range(26)}
        for i, c in enumerate(s):
            if len(d[c]) == 0:
                d[mapping[c]].append(i)
            else:
                ans += i - d[c].pop()
        return ans

# @lc code=end

