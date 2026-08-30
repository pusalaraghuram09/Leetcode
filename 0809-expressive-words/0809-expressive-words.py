class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def stretchy(word):
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                i_start = i
                while i < len(s) and s[i] == s[i_start]:
                    i += 1
                s_count = i - i_start

                j_start = j
                while j < len(word) and word[j] == word[j_start]:
                    j += 1
                w_count = j - j_start

                if s_count < w_count:
                    return False

                if s_count != w_count and s_count < 3:
                    return False

            return i == len(s) and j == len(word)

        return sum(stretchy(word) for word in words)