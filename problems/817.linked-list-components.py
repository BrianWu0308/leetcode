#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        cur = head
        flag = 1
        ans = 0
        while cur:
            if flag == 1 and cur.val in s:
                flag = 0
                ans += 1
            elif flag == 0 and cur.val not in s:
                flag = 1
            cur = cur.next
        return ans




# @lc code=end

