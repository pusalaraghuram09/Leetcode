class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1

        square = [0] * len(nums)
        biggest = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                square[biggest] = nums[left] * nums[left]
                left += 1
            else:
                square[biggest] = nums[right] * nums[right]
                right -= 1
            
            biggest -= 1
        
        return square


        