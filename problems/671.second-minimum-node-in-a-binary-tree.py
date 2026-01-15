#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        min_val = root.val
        ans = float('inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return
            if min_val < node.val < ans:
                ans = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans if ans < float('inf') else -1

# @lc code=end

