class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        ans = len(s)

        for ch in target:
            if ch not in count:
                return 0

            ans = min(ans, count[ch] // target.count(ch))

        return ans