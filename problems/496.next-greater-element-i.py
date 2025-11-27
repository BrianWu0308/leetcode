#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans_dict = {}
        # right -> left ver.
        for x in nums2[::-1]:
            while stack and stack[-1] < x:
                stack.pop()
            if not stack:
                ans_dict[x] = -1
            else:
                ans_dict[x] = stack[-1]
            stack.append(x)
        ans = [ans_dict[x] for x in nums1]
        return ans
        """
        left -> right ver.
        for x in nums2:
            while stack and stack[-1] < x:
                smaller = stack.pop()
                ans_dict[smaller] = x
            stack.append(x)
        while stack:
            ans_dict[stack.pop()] = -1
        """


# @lc code=end

