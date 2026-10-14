class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortMap = {}
        output = []

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in sortMap:
                sortMap[sortedString].append(string)
            else:
                sortMap[sortedString] = [string]
            
        output = (list(sortMap.values()))
        return output
        