class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = 0
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
                currentCount -= 1
                l += 1

        return maxCount


        