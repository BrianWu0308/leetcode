#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        ans = 0
        for x in nums:
            if d[k - x] > 0:
                ans += 1
                d[k - x] -= 1
            else:
                d[x] += 1
        return ans
# @lc code=end

