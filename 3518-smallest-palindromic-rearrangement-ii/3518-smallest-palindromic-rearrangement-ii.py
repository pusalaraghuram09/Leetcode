from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        half = []

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half.extend([ch] * (freq[ch] // 2))

        cnt = Counter(half)
        n = len(half)

        def count_perm(counter):
            total = sum(counter.values())
            res = 1
            rem = total
            for c in counter.values():
                if c:
                    res *= comb(rem, c)
                    rem -= c
                    if res > k:
                        return k + 1
            return res

        if count_perm(cnt) < k:
            return ""

        ans = []

        for _ in range(n):
            for ch in sorted(cnt):
                if cnt[ch] == 0:
                    continue

                cnt[ch] -= 1
                ways = count_perm(cnt)

                if ways >= k:
                    ans.append(ch)
                    break
                else:
                    k -= ways
                    cnt[ch] += 1

        left = "".join(ans)
        return left + mid + left[::-1]