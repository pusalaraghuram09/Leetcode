class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}

        for word in words:
            for ch in word:
                count[ch] = count.get(ch, 0) + 1

        for ch in count:
            if count[ch] % len(words) != 0:
                return False

        return True