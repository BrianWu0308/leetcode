#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        cur = head
        while cur:
            ans = ans * 2 + cur.val  # 或 ans = (ans << 1) | cur.val
            cur = cur.next
        return ans
# @lc code=end

