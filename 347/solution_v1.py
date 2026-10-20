class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))

        res = []

        for i in range(k):
            val = list(freq)[i] 
            res.append(val)

        return res