class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = defaultdict(list)
        
        for str in strs:
            sortedStr = ''.join(sorted(str))
            sorted_map[sortedStr].append(str)
        return list(sorted_map.values())
