from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()#create an empty queue.

    def ping(self, t: int) -> int:
        
        self.queue.append(t)

        start = t - 3000

        while self.queue[0] < start:
            self.queue.popleft()
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)