#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target: # use '> target' to avoid '>= target + 1'
                right = mid - 1
            else:
                left = mid + 1
        if left == len(letters):
            return letters[0]
        return letters[left]
# @lc code=end

