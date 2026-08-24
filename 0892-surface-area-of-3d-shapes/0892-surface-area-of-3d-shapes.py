class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    area += 2

                    area += grid[i][j] * 4

                    if i > 0:
                        area -= 2 * min(grid[i][j], grid[i - 1][j])

                    if j > 0:
                        area -= 2 * min(grid[i][j], grid[i][j - 1])

        return area