#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start != nums[i-1]:
                    ans.append(f'{start}->{nums[i-1]}')
                else:
                    ans.append(str(start))
                start = nums[i]
        if nums[i] == start:
            ans.append(str(start))
        else:
            ans.append(f'{start}->{nums[-1]}')
        return ans

# @lc code=end

