class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) solution in mind, where we store occurrence of
        # each element in HashMap (a.k.a. dict)

        occs = dict()
        for n in nums:
            if n in occs:
                occs[n] += 1
            else:
                occs[n] = 1
        return list(dict(sorted(occs.items(), key = lambda x: x[1], reverse = True)[:k]).keys())
