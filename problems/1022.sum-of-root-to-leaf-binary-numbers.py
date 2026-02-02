#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, cur):
            nonlocal ans
            if node is None:
                return
            val = node.val + cur * 2
            if node.left is None and node.right is None:
                ans += val
            dfs(node.left, val)
            dfs(node.right, val)
        dfs(root, 0)
        return ans
# @lc code=end

