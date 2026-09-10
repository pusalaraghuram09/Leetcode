class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(k):
            removed = set(removable[:k])
            j = 0

            for i in range(len(s)):
                if i in removed:
                    continue

                if j < len(p) and s[i] == p[j]:
                    j += 1

            return j == len(p)

        left, right = 0, len(removable)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right