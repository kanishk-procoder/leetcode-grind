class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        val = 0
        for i in digits:
            val = val*10 + i
        
        val = val + 1
        val_str = str(val)

        dig = []
        dig = [int(ch) for ch in val_str]

        return dig