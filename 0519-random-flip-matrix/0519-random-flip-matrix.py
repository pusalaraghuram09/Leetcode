class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = set()

    def flip(self) -> List[int]:
        import random

        while True:
            index = random.randint(0, self.total - 1)

            if index not in self.flipped:
                self.flipped.add(index)

                return [index // self.n, index % self.n]

    def reset(self) -> None:
        self.flipped.clear()