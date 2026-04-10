class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_one = sorted(s)
        sorted_two = sorted(t)
        if sorted_one == sorted_two:
            return True
        else:
            return False


