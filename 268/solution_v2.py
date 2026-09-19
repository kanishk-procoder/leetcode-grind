class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n*(n+1))/2
        res = int(total_sum-sum(nums))
        return res