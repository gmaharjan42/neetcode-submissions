class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matchMap = {
        ")" : "(", 
        "]" : "[", 
        "}" : "{"
        }
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            
            else:
                if char in matchMap:
                    if len(stack) == 0:
                        return False
                    
                    if stack[-1] == matchMap[char]:
                        stack.pop()
                        
                    else:
                        return False
                    
        if len(stack) == 0:
            return True
        return False