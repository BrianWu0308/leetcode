#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        llsum = 0
        flag = 1
        def dfs(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                nonlocal llsum, flag
                llsum += node.val
                flag = 0
                return
            dfs(node.left)
            flag = 1
            dfs(node.right)
        dfs(root)
        return llsum

# @lc code=end

