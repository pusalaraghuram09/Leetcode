class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappingS = {}
        mappingT = {}

        for c1, c2 in zip(s, t):
            if c1 in mappingS:
                if mappingS[c1] != c2:
                    return False
            else:
                mappingS[c1] = c2

            if c2 in mappingT:
                if mappingT[c2] != c1:
                    return False
            else:
                mappingT[c2] = c1
        return True
                
