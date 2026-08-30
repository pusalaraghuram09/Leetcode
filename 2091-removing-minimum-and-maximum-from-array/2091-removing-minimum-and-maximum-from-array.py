class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        n = len(nums)

        return min(
            right + 1,              # Remove from front
            n - left,              # Remove from back
            left + 1 + n - right   # Remove from both sides
        )