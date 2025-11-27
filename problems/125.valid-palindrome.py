#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ns.lower() for ns in s if ns.isalnum()])
        return s == s[::-1]
# @lc code=end

