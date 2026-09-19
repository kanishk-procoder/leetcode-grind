class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ar = 0
        left = 0
        right = len(height) - 1

        while left < right :
            width = right - left
            high = min(height[left], height[right])
            area = width * high
            max_ar = max(max_ar, area)

            if height[left] < height[right] :
                left += 1
            else :
                right -= 1
        return max_ar