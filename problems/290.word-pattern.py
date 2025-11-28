#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        map_p_s = {}
        map_s_p = {}
        for char_p, char_s in zip(pattern, s):
            if char_p in map_p_s:
                if map_p_s[char_p] != char_s:
                    return False
            else:
                if char_s in map_s_p and map_s_p[char_s] != char_p:
                    return False
                map_p_s[char_p] = char_s
                map_s_p[char_s] = char_p
        return True
# @lc code=end

