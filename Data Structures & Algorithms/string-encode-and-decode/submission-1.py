class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        return encodedString

    def decode(self, s: str) -> List[str]:
        originalList = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            #once we find # we want to slice just the number that is right
            #before it which will give us the length

            length = int(s[i:j])
            #convert to int as well so we can use it

            i = j + 1
            word = s[i: length + i]

            originalList.append(word)
            i = length + i

        return originalList
