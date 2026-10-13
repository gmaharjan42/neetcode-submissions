class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        original = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            strLength = int(s[i:j])
            i = j + 1

            word = s[i: i + strLength]
            i = strLength + i

            original.append(word)
            
        
        return original

            
