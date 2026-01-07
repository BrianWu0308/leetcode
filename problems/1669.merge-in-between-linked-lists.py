#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while tail.next:
            tail = tail.next
        cur1 = list1
        for _ in range(b):
            cur1 = cur1.next
        tail.next = cur1.next
        cur2 = list1
        for _ in range(a - 1):
            cur2 = cur2.next
        cur2.next = list2
        return list1


# @lc code=end

