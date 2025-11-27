#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthese_dict = {')': '(', ']': '[', '}': '{'}
        for item in s:
            if item in {'(', '[', '{'}:
                stack.append(item)
            elif stack and stack[-1] == parenthese_dict[item]:
                stack.pop()
            else:
                return False
        return not stack

# @lc code=end

