# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Create
        left = 1 ## First version
        right = n ## Last version.

        while left <= right: ## Search
            mid = (left + right) // 2 # Find Middle

            if isBadVersion(mid):# Check
                answer = mid   # Save

                right = mid - 1 # Search Left (maybe an earlier bad version)

            else:
                left = mid + 1 # Search Right (bad version is later)

        return answer # Return

        