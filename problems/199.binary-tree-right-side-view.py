#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def dfs(node, h):
            if not node:
                return
            if h == len(ans):
                ans.append(node.val)
            dfs(node.right, h + 1)
            dfs(node.left, h + 1)
        dfs(root, 0)
        return ans
# @lc code=end

