#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for x in range(1, target[-1] + 1):
            ans.append('Push')
            if x != target[i]:
                ans.append('Pop')
            else:
                i += 1
        return ans
# @lc code=end

