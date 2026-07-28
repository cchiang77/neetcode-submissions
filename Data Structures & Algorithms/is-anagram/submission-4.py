class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS, hashT = {}, {}
        for i in s:
            hashS[i] = 1 + hashS.get(i, 0)
        
        for j in t:
            hashT[j] = 1 + hashT.get(j, 0)

        if hashS == hashT:
            return True
        
        return False
        