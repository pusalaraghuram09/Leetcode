class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = {}

        for arr in nums:
            for num in arr:
                count[num] = count.get(num, 0) + 1

        result = []

        for num in count:
            if count[num] == len(nums):
                result.append(num)

        return sorted(result)