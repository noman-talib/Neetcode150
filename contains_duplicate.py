from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mylist = []
        for i in nums:
            if i in mylist:
                return True
            else:
                mylist.append(i)
        return False
