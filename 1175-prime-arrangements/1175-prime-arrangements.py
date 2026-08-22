class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Count prime numbers
        prime_count = 0

        for num in range(2, n + 1):
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_count += 1

        # Prime numbers go in prime positions
        # Non-prime numbers go in non-prime positions
        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result

        return (factorial(prime_count) * factorial(n - prime_count)) % MOD