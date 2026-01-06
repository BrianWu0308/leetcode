#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1) 計算總長度 n
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 2) 計算每段基本長度 q，以及前 r 段要多 1 個節點
        q, r = divmod(n, k)

        ans = []
        cur = head

        # 3) 逐段切割
        for i in range(k):
            part_head = cur
            part_len = q + (1 if i < r else 0)

            if part_len == 0:
                ans.append(None)
                continue

            # 走到本段尾巴（共 part_len 個節點，所以走 part_len-1 步）
            for _ in range(part_len - 1):
                cur = cur.next

            # 斷開並移動到下一段
            next_head = cur.next
            cur.next = None
            ans.append(part_head)
            cur = next_head

        return ans

# @lc code=end

