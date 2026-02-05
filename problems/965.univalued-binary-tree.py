#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left:
            if root.left.val != root.val or not self.isUnivalTree(root.left):
                return False
        if root.right:
            if root.right.val != root.val or not self.isUnivalTree(root.right):
                return False
        return True
# @lc code=end

