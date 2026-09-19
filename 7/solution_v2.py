class Solution:
    def reverse(self, x: int) -> int:
        rev_x = 0
        if x<0 :
            sign = -1
        else :
            sign = 1
        x = x * sign
        while x != 0:
            c = x % 10
            rev_x = rev_x * 10 + c
            x //= 10
        rev_x = rev_x * sign        
        return rev_x if -(2**31) <= rev_x <= (2**31 - 1) else 0