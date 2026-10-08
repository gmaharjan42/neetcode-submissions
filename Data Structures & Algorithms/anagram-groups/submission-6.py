class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputMap = {}

        for string in strs:
            #cat == act, act = ["act", "cat"]
            sortedString = "".join(sorted(string))

            if sortedString not in outputMap:
                outputMap[sortedString] = []
            
            outputMap[sortedString].append(string)

        return list(outputMap.values())