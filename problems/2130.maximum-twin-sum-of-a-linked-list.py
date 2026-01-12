#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        l1, l2 = head, pre
        mx = -1
        while l2:
            mx = max(l1.val + l2.val, mx)
            l1 = l1.next
            l2 = l2.next
        return mx

# @lc code=end

