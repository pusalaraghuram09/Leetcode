class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            # Go backwards so we don't overwrite values
            for j in range(n, 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]