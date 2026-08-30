class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        
        for rank, num in enumerate(sorted(set(arr)), 1):
            ranks[num] = rank
        
        return [ranks[num] for num in arr]