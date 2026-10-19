class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in  nums:
            number = list(str(num))
            if (len(number)%2 == 0):
                count+=1
        return count