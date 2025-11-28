#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        """
        # more effective way
        seen = set()
        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False
        """
# @lc code=end

