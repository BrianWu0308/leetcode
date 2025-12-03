#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b_count = 0
        recolor = 0
        ans = float('inf')
        for i, c in enumerate(blocks):
            if c == 'B':
                b_count += 1
            l = i - k + 1
            if l < 0:
                continue
            recolor = k - b_count
            ans = min(recolor, ans)
            if blocks[l] == 'B':
                b_count -= 1
        return ans

# @lc code=end

