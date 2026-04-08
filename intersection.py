class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mynums1 = set(nums1)
        mynums2 = set(nums2)
        intersection = mynums1.intersection(mynums2)
        myintersection = list(intersection)
        return myintersection