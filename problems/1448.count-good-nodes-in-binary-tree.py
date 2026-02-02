#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, mx):
            nonlocal ans
            if not node:
                return
            if node.val >= mx:
                mx = node.val
                ans += 1
            dfs(node.left, mx)
            dfs(node.right, mx)
        dfs(root, float('-inf'))
        return ans
# @lc code=end

