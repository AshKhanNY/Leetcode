class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using dictionaries once more, you can use the index
        # or key as a pointer to unique dictionary values, where
        # each value is an anagram
        anagrams = dict()
        ans = list()
        i = 0
        for s in strs:
            temp = dict()
            for c in s:
                if c in temp:
                    temp[c] += 1
                else:
                    temp[c] = 1
            if temp in anagrams.values():
                pos = list(anagrams.keys())[list(anagrams.values()).index(temp)]
                ans[pos].append(s)
            else:
                anagrams[i] = temp
                ans.append([s])
                i += 1
        return ans

        
