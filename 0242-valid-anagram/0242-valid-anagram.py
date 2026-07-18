class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts = {}
        countt = {}
        
        for c1, c2 in zip(s, t):
              # Count
            counts[c1] = counts.get(c1, 0) + 1
            countt[c2] = countt.get(c2, 0) + 1

        return counts == countt  # Compare


