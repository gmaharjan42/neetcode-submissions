class Solution:
    def isPalindrome(self, s: str) -> bool:
        condensedS = ""

        for char in s:
            if char.isalnum():
                condensedS += char.lower()
        
        reversedS = condensedS[::-1]

        if condensedS == reversedS:
            return True
        
        return False