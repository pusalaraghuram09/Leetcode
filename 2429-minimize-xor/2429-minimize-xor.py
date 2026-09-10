class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = num2.bit_count()
        x = 0

        # Set bits from most significant to least significant
        # where num1 also has a bit set
        for i in range(31, -1, -1):
            if bits > 0 and (num1 & (1 << i)):
                x |= (1 << i)
                bits -= 1

        # If more bits are needed, use the smallest positions
        for i in range(32):
            if bits > 0 and not (x & (1 << i)):
                x |= (1 << i)
                bits -= 1

        return x