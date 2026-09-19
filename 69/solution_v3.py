class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x

        a = 2
        while (a*a) < x :
            a+=1
        if (a*a) > x:
            return a-1
        elif (a*a) == x:
            return a