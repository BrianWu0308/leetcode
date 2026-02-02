#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        def dfs(node, s):
            nonlocal ans
            if node is None:
                return
            s.append(chr(ord('a') + node.val))
            if node.left is None and node.right is None:
                cur = ''.join(reversed(s))
                if ans is None:
                    ans = cur
                else:
                    ans = min(cur, ans)
            dfs(node.left, s)
            dfs(node.right, s)
            s.pop()
        dfs(root, [])
        return ans
            
# @lc code=end

