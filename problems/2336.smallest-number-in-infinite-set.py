#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.h = []
        heapq.heapify(self.h)
        self.s = set()
        self.current = 0
    def popSmallest(self) -> int:
        if self.h:
            x = heapq.heappop(self.h)
            self.s.add(x)
            return x
        else:
            self.current += 1
            self.s.add(self.current)
            return self.current

    def addBack(self, num: int) -> None:
        if num in self.s:
            heapq.heappush(self.h, num)
            self.s.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

