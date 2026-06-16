class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # they have to be of same length 
        if len(s) != len(t):
            return False
        
        counterDict = {}

        for i in range(len(s)):
            counterDict[s[i]] = counterDict.get(s[i], 0) + 1 
            counterDict[t[i]] = counterDict.get(t[i], 0) - 1 
        
        for key in counterDict:
            if counterDict[key] != 0 :
                return False 
        return True
            
        