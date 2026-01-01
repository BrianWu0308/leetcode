#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        from itertools import accumulate
        d = [0] * (n + 1)
        for first, last, seats in bookings:
            d[first - 1] += seats
            d[last] -= seats
        return list(accumulate(d))[:-1]
        
# @lc code=end

