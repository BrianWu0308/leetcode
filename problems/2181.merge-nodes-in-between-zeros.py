#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = head.next
        while q:
            if q.next.val == 0:
                q.next = q.next.next
                q = q.next
            else:
                q.val += q.next.val
                q.next = q.next.next
        return head.next
# @lc code=end

