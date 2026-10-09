class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        originalList = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1

            word = s[i: length + i]
            i = length + i

            originalList.append(word)
        
        return originalList



