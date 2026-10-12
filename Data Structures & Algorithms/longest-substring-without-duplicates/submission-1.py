class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()
        maxCount = 0
        currentCount = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                currentCount += 1
                if currentCount > maxCount:
                    maxCount = currentCount
            
            else:
                charSet.remove(s[l])
                l += 1
                currentCount -= 1
        
        return maxCount
        

