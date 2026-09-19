class Solution:
    def mySqrt(self, x: int) -> int:
        a = 0
        while (a*a) < x :
            a+=1
        if (a*a) > x:
            return a-1
        elif (a*a) == x:
            return a