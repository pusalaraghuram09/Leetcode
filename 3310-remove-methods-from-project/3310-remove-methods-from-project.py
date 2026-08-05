from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods (reachable from k)
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        # If any outside method invokes a suspicious method,
        # we cannot remove the suspicious group.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Otherwise return the remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans