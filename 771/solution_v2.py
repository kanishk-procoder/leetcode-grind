class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_list = set(jewels)
        res = 0
        freq = {}
        for st in stones:
            if st in jewel_list:
                res+=1
        
        return res