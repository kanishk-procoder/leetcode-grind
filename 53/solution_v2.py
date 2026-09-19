class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0]
        b = nums[0]

        for i in nums[1:] :
            b = max(i,b+i)
            a = max(a,b)
        return a