class Solution:
    def arrangeCoins(self, n: int) -> int:
        comp_sidhi = 0
        coins_left = n
        i=1
        while(coins_left >= i):
            comp_sidhi += 1
            coins_left -= i
            i+=1
        return comp_sidhi
