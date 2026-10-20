class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_list = set(list(jewels))
        res = 0
        freq = {}
        for st in stones:
            freq[st] = freq.get(st, 0) + 1
        
        for s in jewel_list:
            res += freq.get(s, 0)
        
        return res