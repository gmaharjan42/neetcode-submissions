class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashS = {}
        hashT = {}

        for char in s:
            if char in hashS:
                hashS[char] += 1
            else:
                hashS[char] = 1

        for char in t:
            if char in hashT:
                hashT[char] += 1
            else:
                hashT[char] = 1
        
        return hashS == hashT