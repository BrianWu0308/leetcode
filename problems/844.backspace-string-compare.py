#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        temp1 = []
        temp2 = []
        for c in s:
            if c == '#' and temp1:
                temp1.pop()
            elif c != '#':
                temp1.append(c)
        for c in t:
            if c == '#' and temp2:
                temp2.pop()
            elif c != '#':
                temp2.append(c)
        return temp1 == temp2
# @lc code=end

