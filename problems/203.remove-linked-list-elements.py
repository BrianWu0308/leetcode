#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy  # cur 永遠指向「待檢查節點的前一個」

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next  # 刪掉 cur.next
            else:
                cur = cur.next  # 只有不刪時才往前走

        return dummy.next

# @lc code=end

