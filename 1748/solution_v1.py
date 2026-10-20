class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        res = 0
        ele = set(nums)
        freq = {}

        for c in nums:
            freq[c] = freq.get(c, 0) + 1
        
        for c in ele:
            if freq.get(c,0) == 1:
                res+=c
            
        return res