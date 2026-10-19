from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        frequencies = sorted(freq.values())
        
        unique = len(frequencies)

        for count in frequencies:
            if k >= count:
                unique-=1
                k -= count
            else:
                break
        return unique