#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        can_reach_pacific = [[0] * n for _ in range(m)]
        can_reach_atlantic = [[0] * n for _ in range(m)]
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        # dfs on a 2D grid
        def dfs(row: int, col: int, visit: list[list[int]]):
            if visit[row][col]:
                return
            visit[row][col] = 1
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[row][col] <= heights[nr][nc]:
                        dfs(nr, nc, visit)

        for i in range(m):
            dfs(i, 0, can_reach_pacific)
        for i in range(n):
            dfs(0, i, can_reach_pacific)
        for i in range(m):
            dfs(i, n - 1, can_reach_atlantic)
        for i in range(n):
            dfs(m - 1, i, can_reach_atlantic)

        ans = []
        for r in range(m):
            for c in range(n):
                if can_reach_pacific[r][c] and can_reach_atlantic[r][c]:
                    ans.append([r, c])
        return ans
        
# @lc code=end

