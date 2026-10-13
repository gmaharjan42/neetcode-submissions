class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        valuesList = []

        for string in strs:
            sortedString = "".join(sorted(string))
            anagramMap[sortedString].append(string)

        valuesList = list(anagramMap.values())
        return valuesList