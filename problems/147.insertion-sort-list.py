#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        last_sorted = head          # 已排序區間的尾巴
        cur = head.next             # 待插入的節點

        while cur:
            if cur.val >= last_sorted.val:
                # 已經在正確位置（比已排序尾巴還大），直接擴張已排序區間
                last_sorted = cur
                cur = cur.next
            else:
                # 需要把 cur 插入到已排序區間內
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next

                # 先把 cur 從原位置拔掉
                last_sorted.next = cur.next

                # 再把 cur 插入到 prev 後面
                cur.next = prev.next
                prev.next = cur

                # cur 回到下一個待處理節點（last_sorted.next）
                cur = last_sorted.next

        return dummy.next
            
# @lc code=end

