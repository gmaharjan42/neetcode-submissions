class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        currentCount = 0
        maxCount = 0
        charSet = set()
        
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                currentCount += 1
                if currentCount > maxCount:
                    maxCount = currentCount
                r += 1

            else:
                charSet.remove(s[l])
                l += 1
                currentCount -= 1
                
        return maxCount
