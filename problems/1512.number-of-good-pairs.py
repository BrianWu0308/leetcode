#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # ai - aj == 0
        from collections import defaultdict
        freq = defaultdict(int)
        ans = 0
        for x in nums:
            if freq[x] != 0:
                ans += freq[x]
            freq[x] += 1
        return ans
# @lc code=end

