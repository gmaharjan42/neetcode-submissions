class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ga_map = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in ga_map:
                ga_map[sorted_string] = []
            
            ga_map[sorted_string].append(string)
        
        return list(ga_map.values())

