class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        chars = "0123456789abcdef"
        result = ""

        # Handle negative numbers using 32-bit two's complement
        if num < 0:
            num += 2**32

        while num > 0:
            remainder = num % 16
            result = chars[remainder] + result
            num //= 16

        return result