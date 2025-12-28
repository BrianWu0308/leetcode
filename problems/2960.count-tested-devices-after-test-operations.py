#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        dec = 0
        for x in batteryPercentages:
            if x > dec:
                dec += 1
        return dec
        
# @lc code=end

