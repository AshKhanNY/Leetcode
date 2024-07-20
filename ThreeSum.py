class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Asks for a solution set of triplets that add up to 0
        # No duplicates, must be ALL possible triplets
        # We can try to combine our prior knowledge of 2Sum and
        # apply it here. * Requires sorted array *
        ans = []
        nums = sorted(nums)
        i = 0
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + v
                if threeSum == 0:
                    ans.append([nums[l], nums[r], v])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
        return ans