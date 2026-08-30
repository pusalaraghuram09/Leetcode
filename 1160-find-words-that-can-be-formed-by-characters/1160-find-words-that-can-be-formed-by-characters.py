from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available = Counter(chars)
        total = 0

        for word in words:
            count = Counter(word)

            if all(count[c] <= available[c] for c in count):
                total += len(word)

        return total