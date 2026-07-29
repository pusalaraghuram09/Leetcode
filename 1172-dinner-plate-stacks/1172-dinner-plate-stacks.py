from heapq import heappush, heappop

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []
        self.non_empty = []

    def push(self, val: int) -> None:
        while self.available and (
            self.available[0] >= len(self.stacks) or
            len(self.stacks[self.available[0]]) == self.capacity
        ):
            heappop(self.available)

        if not self.available:
            self.stacks.append([])
            idx = len(self.stacks) - 1
            heappush(self.available, idx)
        else:
            idx = self.available[0]

        self.stacks[idx].append(val)
        heappush(self.non_empty, -idx)

        if len(self.stacks[idx]) == self.capacity:
            heappop(self.available)

    def pop(self) -> int:
        while self.non_empty and (
            -self.non_empty[0] >= len(self.stacks) or
            len(self.stacks[-self.non_empty[0]]) == 0
        ):
            heappop(self.non_empty)

        if not self.non_empty:
            return -1

        idx = -self.non_empty[0]
        val = self.stacks[idx].pop()

        if len(self.stacks[idx]) == self.capacity - 1:
            heappush(self.available, idx)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()

        if len(self.stacks[index]) == self.capacity - 1:
            heappush(self.available, index)

        heappush(self.non_empty, -index)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)