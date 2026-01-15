#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        ans = False
        def dfs(node, current_sum):
            nonlocal ans
            if not node or ans:
                # early stop if ans is found
                return
            current_sum += node.val
            if not node.left and not node.right:
                if current_sum == targetSum:
                    ans = True
                return
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        dfs(root, 0)
        return ans
# @lc code=end

