class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}
        
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr not in sorted_map:
                sorted_map[sortedStr] = []
            sorted_map[sortedStr].append(str)
        return list(sorted_map.values())
