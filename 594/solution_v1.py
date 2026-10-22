class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = 0

        for num in freq:
            if num + 1 in freq:
                com = freq.get(num,0)+freq.get(num+1, 0)
                res = max(res, com)

        return res