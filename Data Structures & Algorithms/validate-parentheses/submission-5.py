class Solution:
    def isValid(self, s: str) -> bool:
        # neetcode's solution. 
        stack = []
        closeToOpenMap = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in closeToOpenMap: 
                if stack and stack[-1] == closeToOpenMap[bracket]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False

        

                    


        