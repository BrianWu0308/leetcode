#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_dict = {}
        for char in magazine:
            char_dict[char] = char_dict.get(char, 0) + 1
        for char in ransomNote:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            else:
                return False
        return True
# @lc code=end

