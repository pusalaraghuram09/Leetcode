class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 == s2:
            return 0

        if s1 > s2:
            nums1, nums2 = nums2, nums1

        diff = abs(s1 - s2)

        changes = []

        for x in nums1:
            changes.append(6 - x)

        for x in nums2:
            changes.append(x - 1)

        changes.sort(reverse=True)

        count = 0

        for change in changes:
            diff -= change
            count += 1

            if diff <= 0:
                return count

        return -1
        