class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0     #Step 1: Create the pointers
        right = len(nums) - 1

        while left <= right:  #Step 2: Keep searching

            mid = (left + right) // 2 #Step 3: Find the middle

            if nums[mid] == target: #Step 4: Compare

                return mid #Return the index.

            elif nums[mid] < target: #Step 5: Target is bigger
                left = mid + 1 #Move left

            else:  #step 6: Target is smaller
                right = mid - 1 #Move the right

        return -1  #The target doesn't exist.