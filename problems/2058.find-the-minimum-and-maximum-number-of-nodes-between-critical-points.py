#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDis, last, first = inf, 0, 0
        a,b,c = head, head.next, head.next.next
        i = 1
        while c:
            if c.val < b.val > a.val or a.val > b.val < c.val:
                if first == 0:
                    first = i
                if last > 0 and i - last < minDis:
                    minDis = i - last
                last = i
            a, b, c, i = b, c, c.next, i + 1
        return [minDis, last - first] if last != first else [-1, -1]
# @lc code=end

