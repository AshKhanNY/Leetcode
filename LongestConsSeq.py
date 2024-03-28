class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Idea is to keep a nums set where we check
        # every number and see if they're a start of a
        # sequence (can check if it has left neighbor)
        chains = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in chains:
                chain = 1
                while n+chain in chains:
                    chain += 1
                longest = max(longest, chain)
        return longest