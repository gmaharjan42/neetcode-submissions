class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = {}
        outputList = []

        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr not in anagramList:
                anagramList[sortedStr] = []
            anagramList[sortedStr].append(string)
        
        outputList = list(anagramList.values())
        return outputList