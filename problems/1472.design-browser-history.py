#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        self.s = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        del self.s[self.current + 1:]
        self.s.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        steps = min(steps, self.current)
        self.current -= steps
        return self.s[self.current]

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.s) - 1 - self.current)
        self.current += steps
        return self.s[self.current]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

