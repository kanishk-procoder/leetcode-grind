class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}

        for i, x in enumerate(nums):
            if x in last_seen:
                res = abs(i - last_seen[x])
                if k >= res:
                    return True
            last_seen[x] = i
        
        return False
