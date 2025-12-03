#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = count = 0
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for i, c in enumerate(s):
            if c in vowel:
                count += 1
            left = i - k + 1
            if left < 0:
                continue
            ans = max(ans, count)
            if s[left] in vowel:
                count -= 1
        return ans
# @lc code=end

