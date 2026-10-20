class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        x = len(freq)
        unique_freq = set(freq.values())
        y = len(unique_freq)

        if x==y:
            return True
        else:
            return False