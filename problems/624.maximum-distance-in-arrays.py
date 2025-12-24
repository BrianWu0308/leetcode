#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = (float('inf'), -1)
        ans = 0
        for row in arrays:
            for ele in row:
                if ele < min_val:
                    min_val = (ele, row)
                ans = max(abs(ele - min_val), ans)
        return ans


# @lc code=end

