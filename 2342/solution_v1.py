class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        res = -1
        freq = {}

        idx = {}

        for x in nums:
            dig_sum = sum(int(digit) for digit in str(x))
            if dig_sum in freq:
                res = max(res,x + idx.get(dig_sum,0))
                idx[dig_sum] = max(x, idx.get(dig_sum, 0))
            else:
                idx[dig_sum] = x
            
            freq[dig_sum] = freq.get(dig_sum,0)+ 1

        return res