class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, x in enumerate(nums):
            if x != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1