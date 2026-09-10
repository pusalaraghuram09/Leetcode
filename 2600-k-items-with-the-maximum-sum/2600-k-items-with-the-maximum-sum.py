class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k

        ans = numOnes
        k -= numOnes

        # Zeros don't change the sum
        if k <= numZeros:
            return ans

        k -= numZeros

        # Remaining items are -1
        return ans - k