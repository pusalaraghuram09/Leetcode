class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        count = 0
        max_length = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in first:
                max_length = max(max_length, i - first[count])
            else:
                first[count] = i

        return max_length