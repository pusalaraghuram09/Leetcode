class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if board[r][c] != "O":
                return

            # Mark as safe
            board[r][c] = "#"

            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # 1. Find O's on the border
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # 2. Convert surrounded O's to X
        # 3. Convert safe # back to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"