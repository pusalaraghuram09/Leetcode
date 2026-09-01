class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)

        # Maximum moves
        max_moves = max(
            stones[-1] - stones[1],
            stones[-2] - stones[0]
        ) - (n - 2)

        # Minimum moves
        min_moves = n
        left = 0

        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1

            in_window = right - left + 1

            # Special case: n-1 consecutive stones with one empty space
            if in_window == n - 1 and stones[right] - stones[left] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - in_window)

        return [min_moves, max_moves]