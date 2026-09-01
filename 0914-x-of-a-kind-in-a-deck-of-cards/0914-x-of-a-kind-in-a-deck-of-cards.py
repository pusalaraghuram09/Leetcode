class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        
        counts = Counter(deck).values()
        
        g = 0
        for count in counts:
            g = gcd(g, count)
        
        return g >= 2