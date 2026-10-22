class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        freq = {}

        for a in nums1:
            for b in nums2:
                pair_sum = a+b


                freq[pair_sum] = freq.get(pair_sum, 0) + 1

        count = 0

        for c in nums3:
            for d in nums4:
                pair_sum = c+d

                target = 0-pair_sum

                count+=freq.get(target, 0)

        return count