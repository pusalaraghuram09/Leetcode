class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted((num, i) for i, num in enumerate(nums))
        result = nums[:]

        start = 0

        for i in range(1, n + 1):
            if i == n or pairs[i][0] - pairs[i - 1][0] > limit:
                indices = sorted(pairs[j][1] for j in range(start, i))
                values = [pairs[j][0] for j in range(start, i)]

                for index, value in zip(indices, values):
                    result[index] = value

                start = i

        return result