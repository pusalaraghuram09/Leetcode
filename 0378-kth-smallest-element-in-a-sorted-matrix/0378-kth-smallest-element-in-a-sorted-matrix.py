class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq

        heap = []

        n = len(matrix)

        # Put the first element of every row
        for r in range(n):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        # Remove smallest k times
        for _ in range(k):
            value, row, col = heapq.heappop(heap)

            # Add next element from the same row
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return value