class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        prev = 1

        for scan in range(1, len(nums)):
            if nums[scan] != nums[scan - 1]:
                nums[prev] = nums[scan]
                prev += 1
        return prev



        