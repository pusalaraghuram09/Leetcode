class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug = set()

        for r, c in dig:
            dug.add((r, c))

        ans = 0

        for r1, c1, r2, c2 in artifacts:
            found = True

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        found = False
                        break

                if not found:
                    break

            if found:
                ans += 1

        return ans