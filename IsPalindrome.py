class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Idea is to use double pointers to check if the string
        # has mirror chars
        s = s.upper()
        def checkValidAlphanumeric(ch: str) -> bool:
            c = ord(ch)
            if (c >= ord('a') and c <= ord('z')) or (c >= ord('A') and c <= ord('Z')) or (c >= ord('0') and c <= ord('9')):  
                return True
            else: 
                return False
        i = 0
        j = len(s) - 1
        while j >= i:
            if not checkValidAlphanumeric(s[i]):
                i += 1
                continue
            if not checkValidAlphanumeric(s[j]):
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True