class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        ans = -1

        for num in count:
            if count[num] == num:
                ans = max(ans, num)

        return ans