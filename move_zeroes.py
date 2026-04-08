class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        mynums = []
        for i in nums[:]:
            if i == 0:
                mynums.append(i)
                nums.remove(i)
        nums.extend(mynums)
        return nums