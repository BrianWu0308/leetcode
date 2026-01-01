#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        while len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

