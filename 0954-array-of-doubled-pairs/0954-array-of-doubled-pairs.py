class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter

        count = Counter(arr)

        for x in sorted(count, key=abs):
            if count[x] == 0:
                continue

            if count[2 * x] < count[x]:
                return False

            count[2 * x] -= count[x]

        return True