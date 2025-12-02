#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while left <= right and top <= bottom:
            
            # 往右
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1
            if top > bottom:
                break

            # 往下
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # 往左
            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom:
                break

            # 往上
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans
            
# @lc code=end

