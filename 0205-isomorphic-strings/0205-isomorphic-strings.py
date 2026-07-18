class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create two Hash Maps: one for s -> t and one for t -> s.
        mappingS = {} 
        mappingT = {}

        for c1, c2 in zip(s, t):    # Read one character from both zip=strings together.

            if c1 in mappingS:        # Check if c1 already has a mapping.

                if mappingS[c1] != c2:  # Return False if the mapping is different.
                    return False
                     
            else:                        # Save a new mapping.
                mappingS[c1] = c2

            if c2 in mappingT:          # Check if c2 already has a reverse mapping.

                if mappingT[c2] != c1:  
                    return False

            else:
                mappingT[c2] = c1        # Save a new reverse mapping.

        return True                   # No conflicts found.
                
