#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) # avoid repeated computations
        for i in range(0, n // 2):
            temp = s[i]
            s[i] = s[(n - 1) - i]
            s[(n - 1) - i] = temp
        """
        # tuple swap
        for i in range(0, n // 2):
            s[i], s[(n - 1) - i] = s[(n - 1) - i], s[i]
        """
        """
        # two pointers
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        """
# @lc code=end

