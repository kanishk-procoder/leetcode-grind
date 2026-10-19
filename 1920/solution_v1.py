class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            x = nums[i]
            ans.append(nums[x])

        return ans