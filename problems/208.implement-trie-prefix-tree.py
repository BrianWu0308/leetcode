#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    __slots__ = 'son', 'end'
    # 代表這個 Node 只會拿來放 child pointers (son) 跟是否為完整字 (end)，
    # 其他任何東西一律不准加，省記憶體

    def __init__(self):
        self.son = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:  # 无路可走？
                cur.son[c] = Node()  # 那就造路！
            cur = cur.son[c]
        cur.end = True

    def find(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:  # 道不同，不相为谋
                return 0
            cur = cur.son[c]
        # 走过同样的路（2=完全匹配，1=前缀匹配）
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

