class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1

        while even < len(nums) and odd < len(nums):

            # Find an even number for even index
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2

            # Find an odd number for odd index
            while odd < len(nums) and nums[odd] % 2 == 1:
                odd += 2

            # Swap incorrect positions
            if even < len(nums) and odd < len(nums):
                nums[even], nums[odd] = nums[odd], nums[even]

        return nums