class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        freq = {}
        res = 0
        MOD = 10**9 + 7
        for num in nums:
            rev = int(str(num)[::-1])

            key = num-rev
            if key in freq:
                res += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1


        return res%MOD
        

