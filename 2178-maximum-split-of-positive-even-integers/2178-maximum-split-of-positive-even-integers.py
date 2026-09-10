class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []

        result = []
        num = 2

        while finalSum >= num:
            result.append(num)
            finalSum -= num
            num += 2

        if finalSum > 0:
            result[-1] += finalSum

        return result