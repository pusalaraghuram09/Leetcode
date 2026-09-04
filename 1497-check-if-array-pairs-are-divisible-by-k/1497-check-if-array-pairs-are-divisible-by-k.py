class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = {}

        for num in arr:
            r = num % k
            remainder[r] = remainder.get(r, 0) + 1

        for r in remainder:
            if r == 0:
                if remainder[r] % 2 != 0:
                    return False
            else:
                if remainder.get(r, 0) != remainder.get(k - r, 0):
                    return False

        return True