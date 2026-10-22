
class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:

        freq = {}

        # Step 1: Count each remainder
        for num in arr:
            rem = num%k
            freq[rem] = freq.get(rem, 0) + 1

        # Step 2: Check whether every remainder has
        # enough complementary remainders
        for rem in freq:

            # Remainder 0 must occur an even number of times
            if rem == 0:
                if freq.get(rem, 0)%2 != 0:
                    return False

            else:
                # Find the complementary remainder
                complement = k-rem

                # Their frequencies must match
                if freq.get(rem, 0) != freq.get(complement, 0):
                    return False

        return True
