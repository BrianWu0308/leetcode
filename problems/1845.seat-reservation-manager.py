#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.current = 0
        self.h = []
        heapq.heapify(self.h)

    def reserve(self) -> int:
        if self.h:
            return heapq.heappop(self.h)
        else:
            self.current += 1
            return self.current

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

