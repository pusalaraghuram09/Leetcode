class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        sorted_nums = sorted(nums1)
        total = 0
        best_gain = 0
        
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total += diff
            
            # Binary search for closest value to b
            left, right = 0, len(sorted_nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if sorted_nums[mid] < b:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left < len(sorted_nums):
                best_gain = max(best_gain, diff - abs(sorted_nums[left] - b))
            
            if right >= 0:
                best_gain = max(best_gain, diff - abs(sorted_nums[right] - b))
        
        return (total - best_gain) % MOD