class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.freq = {}
        for num in nums2:
            self.freq[num] = self.freq.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        new = old + val

        self.freq[old] -= 1
        self.freq[new] = self.freq.get(new, 0) + 1

        self.nums2[index] = new

    def count(self, tot: int) -> int:
        res = 0

        for num in self.nums1:
            rem = tot - num
            res += self.freq.get(rem, 0)

        return res