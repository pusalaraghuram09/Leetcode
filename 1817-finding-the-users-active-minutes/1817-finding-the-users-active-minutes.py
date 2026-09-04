class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}

        for user, minute in logs:
            if user not in users:
                users[user] = set()
            users[user].add(minute)

        answer = [0] * k

        for minutes in users.values():
            count = len(minutes)
            answer[count - 1] += 1

        return answer