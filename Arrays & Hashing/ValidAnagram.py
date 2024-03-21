class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # what defines an anagram pair?
        # same number of occurences of each character
        # no more, no less

        hashMapS = dict()
        hashMapT = dict()
        for i in range(len(s)):
            if s[i] in hashMapS:
                hashMapS[s[i]] += 1
            else:
                hashMapS[s[i]] = 1
            if t[i] in hashMapT:
                hashMapT[t[i]] += 1
            else:
                hashMapT[t[i]] = 1
        return hashMapS == hashMapT