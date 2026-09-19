class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mis_num = 0
        nums.sort()
        for i in nums:
            if (i==mis_num):
                mis_num += 1
            else:
                break
        
        return mis_num