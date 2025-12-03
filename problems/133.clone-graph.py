#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        from collections import deque
        # deep copy every nodes and edges
        clones = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            clone = clones[cur]
            for neighbor in cur.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone.neighbors.append(clones[neighbor])
        return clones[node]

# @lc code=end

