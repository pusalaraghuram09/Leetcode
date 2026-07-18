class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mappingS = {} # Create
        mappingW = {}

        words = s.split() # Split

        if len(pattern) != len(words):  # Validate
            return False
        
        for c1, c2 in zip(pattern, words): # Pair character and word.
         
            if c1 in mappingS:       # Check
                if mappingS[c1] != c2:    # Compare
                    return False
            else:
                mappingS[c1] = c2   # Save

            if c2 in mappingW:
                if mappingW[c2] != c1:
                    return False
            else:
                mappingW[c2] = c1

        return True 
        