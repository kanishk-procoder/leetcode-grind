class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        lastword = arr[-1]

        res = len(lastword)

        return res
