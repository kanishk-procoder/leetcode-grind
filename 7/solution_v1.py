class Solution:
    def reverse(self, x: int) -> int:
        rev_x = 0
        if x<0 :
            x = 0 - x
            while x != 0:
                c = x % 10
                rev_x = rev_x * 10 +c
                x //= 10
            rev_x = 0 - rev_x
        else :
            while x != 0:
                c = x % 10
                rev_x = rev_x * 10 + c
                x //= 10
        return rev_x if -(2**31) <= rev_x <= (2**31 - 1) else 0