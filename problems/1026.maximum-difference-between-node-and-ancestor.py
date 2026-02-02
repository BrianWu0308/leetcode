#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node, mx, mn):
            nonlocal ans
            if node is None:
                return
            mx = max(node.val, mx)
            mn = min(node.val, mn)
            ans = max(mx - mn, ans)
            dfs(node.left, mx, mn)
            dfs(node.right, mx, mn)
        dfs(root, root.val, root.val)
        return ans

# @lc code=end

