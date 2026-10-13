class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()
        
        reversedS = newS[::-1]

        if reversedS == newS:
            return True
        return False