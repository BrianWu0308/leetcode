#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next=head)
        slow = fast = head
        s = []
        while fast and fast.next:
            s.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != s.pop():
                return False
            slow = slow.next
        return True

        
# @lc code=end

