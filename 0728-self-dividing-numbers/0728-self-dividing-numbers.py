class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for num in range(left, right + 1):
            x = num
            valid = True

            while x > 0:
                digit = x % 10

                # Cannot contain 0
                if digit == 0:
                    valid = False
                    break

                # Digit must divide the number
                if num % digit != 0:
                    valid = False
                    break

                x //= 10

            if valid:
                result.append(num)

        return result