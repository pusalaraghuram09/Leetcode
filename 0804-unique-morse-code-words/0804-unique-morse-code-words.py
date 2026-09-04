class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        unique = set()

        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            unique.add(code)

        return len(unique)