class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter

        c1 = Counter(basket1)
        c2 = Counter(basket2)

        all_fruits = set(c1) | set(c2)
        min_val = min(basket1 + basket2)

        extra = []

        for fruit in all_fruits:
            diff = c1[fruit] - c2[fruit]

            if diff % 2 != 0:
                return -1

            if diff > 0:
                extra += [fruit] * (diff // 2)
            elif diff < 0:
                extra += [fruit] * (-diff // 2)

        extra.sort()

        return sum(min(x, 2 * min_val) for x in extra[:len(extra) // 2])