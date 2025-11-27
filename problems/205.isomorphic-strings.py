#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_t = {}
        map_t_s = {}
        for char_s, char_t in zip(s, t):
            if char_s in map_s_t:
                if char_t != map_s_t[char_s]:
                    return False
            else:
                if char_t in map_t_s and map_t_s[char_t] != char_s:
                    return False
                map_s_t[char_s] = char_t
                map_t_s[char_t] = char_s
        return True
# @lc code=end

