class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}

        for row in grid:
            key = tuple(row)
            rows[key] = rows.get(key, 0) + 1

        count = 0
        n = len(grid)

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))

            if col in rows:
                count += rows[col]

        return count