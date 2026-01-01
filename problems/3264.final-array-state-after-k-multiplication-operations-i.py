#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq
        h = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            v, i = heapq.heappop(h)
            v *= multiplier
            nums[i] = v
            heapq.heappush(h, (v, i))
        return nums
# @lc code=end

