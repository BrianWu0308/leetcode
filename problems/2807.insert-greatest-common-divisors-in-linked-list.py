#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head.next
        while b:
            gcd = math.gcd(a.val, b.val)
            new = ListNode(gcd, next=b)
            a.next = new
            a = a.next.next
            b = b.next
        return head

# @lc code=end

