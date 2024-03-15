class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can use an auxillary var to store products of each
        # index as we go along the first pass.
        size = len(nums)
        ans = [1 for i in range(size)]
        prod = 1

        for i in range(1, size):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(1, size):
            prod = prod * nums[size-i]
            ans[size-i-1] = ans[size-i-1] * prod
        
        return ans
            
