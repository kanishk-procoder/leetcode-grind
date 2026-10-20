class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_count = {}
        
        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1

        count = 0

        for c in range(len(grid)):
            column = []

            for r in range(len(grid)):
                column.append(grid[r][c])
            
            count += row_count.get(tuple(column), 0)

        return count
        