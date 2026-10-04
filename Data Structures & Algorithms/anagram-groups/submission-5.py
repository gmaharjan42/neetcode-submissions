class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #this map stores a sorted version of the string as the key
        #and a list of strings that are anagrams of that sorted string
        #as the values
        sortedStringMap = defaultdict(list)

        #now i want to iterate through the array of strings
        for str in strs:
            #first i want to make a variable that will have the sorted
            #version of the current string, and connect the spaces instead
            #of having the characters show up seperated with commas
            sortedString = "".join(sorted(str))

            #then i want to make that sorted string the key for my hashmap
            #while assigning the current string that the for loop is on
            #to that sorted string (since it got sorted from the characters
            #from the current string)

            sortedStringMap[sortedString].append(str)

        #since the hashmap will now iterate through the whole list and append
        #all the sorted anagrams as values of the list we can just make it so 
        #the final hashmap gets returned with only the values showing as a list
        return list(sortedStringMap.values())


        