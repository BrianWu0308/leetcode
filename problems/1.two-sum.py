#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        对于 双变量问题, 例如两数之和ai + aj = t转换成单变量问题, 
        也就是在aj左边查找是否有ai = t - aj, 
        这可以用哈希表维护。
        我把这个技巧叫做 枚举右，维护左。
        """
        target_dict = {}
        for i, item in enumerate(nums):
            if target - item in target_dict:
                return [i, target_dict[target - item]]
            else:
                target_dict[item] = i


# @lc code=end

