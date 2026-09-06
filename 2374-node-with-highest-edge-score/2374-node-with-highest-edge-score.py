class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = [0] * len(edges)

        for i in range(len(edges)):
            score[edges[i]] += i

        max_score = -1
        answer = 0

        for i in range(len(edges)):
            if score[i] > max_score:
                max_score = score[i]
                answer = i

        return answer