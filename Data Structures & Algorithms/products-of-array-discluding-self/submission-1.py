class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i want to create 3 arrays, one for prefix one for suffix
        # and one for output
        output, prefix, suffix = [], [], []
        
        #first lets do prefix (left)
        prefix = [0] * len(nums) #populate prefix with initial values
        
        prefix[0] = 1 #base case: nothing before first index so make it 1

        for i in range(1, len(nums)): #goes from 1-4 for example since 0 is base case
            prefix[i] = prefix[i - 1] * nums[i - 1]
                        #previous prefix value * previous nums value
        
        #second lets do suffix (right)
        suffix = [0] * len(nums) #populate it 
        suffix[len(nums) - 1] = 1 #another base case, nothing after last element so assign it as 1 

        for i in range(len(nums) - 2, -1, -1):
                        #starts right before last element and goes back by 1 until 0 is reached
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        #now lets put these in output array for answer

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        
        return output




        