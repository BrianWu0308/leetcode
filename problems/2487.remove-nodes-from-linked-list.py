#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        dummy = ListNode(next=None)
        cur = dummy
        for node in stack:
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next


# @lc code=end

