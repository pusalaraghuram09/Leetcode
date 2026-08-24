class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        xy = 0
        yz = 0
        zx = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1

            yz += max(grid[i])

        for j in range(n):
            max_height = 0

            for i in range(n):
                max_height = max(max_height, grid[i][j])

            zx += max_height

        return xy + yz + zx