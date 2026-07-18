class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = set(nums1) #Python converts the list into a set.

        ans = set() #Create an empty set.

        for num in nums2: 
            if num in seen: #Check if the current number exists in nums1.

                ans.add(num)  # If it exists, add it to the answer set.
                            # A set automatically ignores duplicates.

        return list(ans) # Convert the set into a list because
        # the problem expects a List[int] as output.