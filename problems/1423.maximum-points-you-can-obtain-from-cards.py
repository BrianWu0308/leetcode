#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        cur_sum = 0
        ans = 0
        for i in range(n - k, n + k):
            cur_sum += cardPoints[i % n]
            l = i - k + 1
            if l < n - k:
                continue
            ans = max(cur_sum, ans)
            cur_sum -= cardPoints[l % n]
        return ans

            

# @lc code=end

