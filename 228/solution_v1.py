class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
            
        i = nums[0]
        j = nums[0]+1
        list1 = []
        for num in range(1,len(nums)):
            if ( j == nums[num]):
                j+=1
            else:
                list1.append([i,j-1])
                i = nums[num]
                j = nums[num]+1
            
            if(j >= nums[-1]):
                j = nums[-1]
                list1. append([i,j])
                break
        result = []
        for i in list1:
            if (i[0] == i[1]):
                res = str(i[0])
            else:
                res = str(i[0]) + "->" + str(i[1])

            result.append(res)
        return result