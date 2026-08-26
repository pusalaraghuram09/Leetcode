class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted(str(n))

        for i in range(31):
            power = 2 ** i

            if sorted(str(power)) == target:
                return True

        return False