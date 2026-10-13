class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        valuesList = []

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in anagramMap:
                anagramMap[sortedString] = []
            anagramMap[sortedString].append(string)

        valuesList = list(anagramMap.values())
        return valuesList