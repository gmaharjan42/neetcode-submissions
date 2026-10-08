class Solution:

    def encode(self, strs: List[str]) -> str:
        #start with empty string (will be needed later)
        encodedString = ""

        #iterate through each string in the list
        for string in strs:
            #append the length of the string and a #
            #as well as the string itself, this will be the encoded
            #word
            encodedString += str(len(string)) + "#" + string
        #after the for loop is done, all of the words in the list
        #will be combined into the encodedString var
        return encodedString

    def decode(self, s: str) -> List[str]:
        originalList = []
        i = 0
        #we are using two pointer for this

        #this while loop will run until i reaches the last index of the encoded
        #string
        while i < len(s):
            #j will keep track of where the # delimiter will be
            j = i
            #when searching for #, keep incrementing j until # is found
            while s[j] != "#":
                j += 1
            
            #once # is found move onto figuring out what the length
            #of the current word was; we will figure this out by looking 
            #at the number we put in the encoded string

            #we will get this number usable by slicing s[i] up until s[j], 
            #which will give us just the number as an int that we can use

            length = int(s[i:j])

            #after we find the length we want to move i right after j and slice
            #up until the length we finally just converted into an int

            i = j + 1 #puts i right at the start of the word

            word = s[i : i + length] #this slices from s[i] up until the next
            #number in the encoded string which signals the end of the word
            #and the start of the next word

            #once getting the word, we should now append the word into the
            #original list

            originalList.append(word)
            #then we should update i to be right after the end of the current word
            i = i + length 

        return originalList


