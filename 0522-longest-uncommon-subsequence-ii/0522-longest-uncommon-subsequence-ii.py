class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(a, b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            found = False
            for j in range(len(strs)):
                if i != j and isSubsequence(strs[i], strs[j]):
                    found = True
                    break
            if not found:
                return len(strs[i])

        return -1