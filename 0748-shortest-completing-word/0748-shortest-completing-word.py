class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = {}

        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1

        answer = None

        for word in words:
            count = {}

            for ch in word.lower():
                count[ch] = count.get(ch, 0) + 1

            valid = True

            for ch in need:
                if count.get(ch, 0) < need[ch]:
                    valid = False
                    break

            if valid:
                if answer is None or len(word) < len(answer):
                    answer = word

        return answer