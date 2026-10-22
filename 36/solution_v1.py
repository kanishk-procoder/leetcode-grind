class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row check
        for row in board:
            freq = {}
            for num in row:
                if num!=".":
                    freq[num] = freq.get(num, 0) + 1
                
                if freq.get(num, 0) > 1:
                    return False
        
        for col in range(len(board)):
            freq = {}
            for row in range(len(board)):
                num = board[row][col]
                if num!=".":
                    freq[num] = freq.get(num, 0) + 1
                
                if freq.get(num, 0) > 1:
                    return False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                freq = {}

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num = board[i][j]

                        if num != ".":
                            freq[num] = freq.get(num, 0) + 1

                            if freq[num] > 1:
                                return False
        
        return True
