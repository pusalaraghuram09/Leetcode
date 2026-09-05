class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        ans = 0

        for freq in count.values():
            if freq == 1:
                return -1

            ans += freq // 3

            if freq % 3 != 0:
                ans += 1

        return ans