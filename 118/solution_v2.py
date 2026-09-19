class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if (numRows == 0): return res
        res.append([1])
        if (numRows == 1): 
            return res
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
