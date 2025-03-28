class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Use Moore's counting algo to figure out
        # frequency of dominent element
        de = nums[0]
        freq = 1
        for i in range(1, len(nums)):
            if nums[i] == de:
                freq += 1
            else:
                freq -= 1
            # choose new dom element
            if freq == 0:
                de = nums[i]
                freq += 1
        # Find how often the dom element appears
        freq = 0
        for n in nums:
            if n == de:
                freq += 1
        # Locate best region to split at, given freq
        preFreq = 0
        for i in range(0, len(nums) - 1):
            if nums[i] == de:
                preFreq += 1
                freq -= 1
            if preFreq > (i + 1) // 2 and freq > (len(nums) - i - 1) // 2:
                return i
        return -1

        