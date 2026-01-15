#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = float('inf')
        def dfs(node, h):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans = min(h, ans)
                return
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)
        dfs(root, 1)
        return ans
        # Alternative:
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# @lc code=end

