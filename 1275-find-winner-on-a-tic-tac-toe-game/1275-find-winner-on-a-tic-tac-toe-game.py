class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = set()
        B = set()

        for i, move in enumerate(moves):
            if i % 2 == 0:
                A.add(tuple(move))
            else:
                B.add(tuple(move))

        lines = [
            {(0, 0), (0, 1), (0, 2)},
            {(1, 0), (1, 1), (1, 2)},
            {(2, 0), (2, 1), (2, 2)},
            {(0, 0), (1, 0), (2, 0)},
            {(0, 1), (1, 1), (2, 1)},
            {(0, 2), (1, 2), (2, 2)},
            {(0, 0), (1, 1), (2, 2)},
            {(0, 2), (1, 1), (2, 0)}
        ]

        for line in lines:
            if line <= A:
                return "A"
            if line <= B:
                return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"