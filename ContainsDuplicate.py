class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempSet = set()
        for n in nums:
            if n in tempSet:
                return True
            tempSet.add(n)
        return False