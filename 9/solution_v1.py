class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = 0
        div = x
        if x<0:
            return False
        elif x == 0:
            return True
        else:
            while x != 0 :
                c = x % 10
                rev_x = rev_x * 10 + c
                x //= 10
            if(div == rev_x):
                return True
            else:
                return False
