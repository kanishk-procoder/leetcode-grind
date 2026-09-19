class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        for i in nums:
            if i==0:
                count_zero+=1
        
        i=0
        while(count_zero!=0):
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)
                count_zero-=1
            else:
                i+=1
        