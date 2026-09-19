class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums)
        for i in range(len(nums)):
            if(nums[i] >= target):
                res = i
                break
        return res