#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        s = []
        for x in pushed:
            s.append(x)
            while s and s[-1] == popped[idx]:
                s.pop()
                idx += 1
        return not s
        
# @lc code=end

