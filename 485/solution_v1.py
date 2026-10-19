class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if nums:
            max_count = 1
            count = 1
            for i in range(1,len(nums)):
                if(nums[i] == nums[i-1]):
                    count += 1
                else:
                    count = 1
                
                max_count = max(count, max_count)
            
            return max_count
        
        else:
            return 0