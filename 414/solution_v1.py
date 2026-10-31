class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        numset = set(nums)
        numset = sorted(numset, reverse = True)
        if(len(numset)<3):
            return numset[0]
        else:
            return numset[2]