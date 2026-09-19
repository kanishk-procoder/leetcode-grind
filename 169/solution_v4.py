class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        freq = 1
        nums.sort()
        ele = nums[0]

        for i in range(1,n):
            if(nums[i] == nums[i-1]):
                freq+=1
            else:
                ele = nums[i]
                freq = 1
            
            if (freq > n/2):
                return ele
        
        return ele