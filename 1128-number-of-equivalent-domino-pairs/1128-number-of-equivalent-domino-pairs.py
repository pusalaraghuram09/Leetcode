class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        pairs = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))

            pairs += count.get(key, 0)
            count[key] = count.get(key, 0) + 1

        return pairs