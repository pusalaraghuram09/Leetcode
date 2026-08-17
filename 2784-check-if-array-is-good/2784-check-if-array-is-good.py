class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        return len(nums) == n + 1 and nums.count(n) == 2 and all(
            nums.count(i) == 1 for i in range(1, n)
        )