#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, p_val, g_val):
            nonlocal ans
            if node is None:
                return
            if g_val is not None and g_val % 2 == 0:
                ans += node.val
            dfs(node.left, node.val, p_val)
            dfs(node.right, node.val, p_val)
        dfs(root, None, None)
        return ans
# @lc code=end

