class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix = []
        total = 0

        for num in nums:
            total += num
            prefix.append(total)

        ans = []

        for q in queries:
            left, right = 0, len(prefix)

            while left < right:
                mid = (left + right) // 2

                if prefix[mid] <= q:
                    left = mid + 1
                else:
                    right = mid

            ans.append(left)

        return ans