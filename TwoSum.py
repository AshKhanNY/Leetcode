class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can do a compliment approach to this
        # O(n) - n being the size of List[int] nums
        # Use target as means to find "matching" pair
        # Keep track of all compliments using HashMap
        hashSet = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashSet:
                return [i, hashSet[target - nums[i]]]
            hashSet[nums[i]] = i


        