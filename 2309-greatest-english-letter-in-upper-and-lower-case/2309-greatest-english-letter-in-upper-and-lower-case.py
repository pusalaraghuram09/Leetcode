class Solution:
    def greatestLetter(self, s: str) -> str:
        for c in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if c in s and c.lower() in s:
                return c

        return ""