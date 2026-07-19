class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0 #give 
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x: ## Perfect Square
                return mid

            elif mid * mid < x:  # Square is Too Small
                answer = mid # Save current valid answer.
                left = mid + 1 # Search Right for a bigger answer.
                
            else:
                right = mid - 1
        return answer
        