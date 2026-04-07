class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mynums = {}  # changed: store num -> index instead of a list
        for i, num in enumerate(nums):  # changed: track index with enumerate
            if num in mynums and i - mynums[num] <= k:  # changed: check distance
                return True
            mynums[num] = i  # changed: update index of num
        return False