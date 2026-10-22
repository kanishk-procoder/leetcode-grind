class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = 0
        unique = {}

        for x in arr:
            unique[x] = unique.get(x, 0) + 1

        for x in arr:
            if unique.get(x,0) == 1:
                count += 1
            if count==k:
                return x
        
        return ""
