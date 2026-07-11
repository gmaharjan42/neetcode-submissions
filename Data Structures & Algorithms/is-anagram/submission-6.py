class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        charCountInS = {}
        charCountInT = {}

        for char in s:
            if char in charCountInS:
                charCountInS[char] += 1
            else:
                charCountInS[char] = 1
        
        for char in t:
            if char in charCountInT:
                charCountInT[char] += 1
            else:
                charCountInT[char] = 1
        
        return charCountInS == charCountInT