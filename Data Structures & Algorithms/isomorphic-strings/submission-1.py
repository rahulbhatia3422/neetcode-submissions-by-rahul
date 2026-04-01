# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return len(set(zip(s, t))) == len(set(s)) == len(set(t))

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        mapST, mapTS = {}, {}
        
        for c1, c2 in zip(s, t):
            if mapST.get(c1, c2) != c2 or mapTS.get(c2, c1) != c1:
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        
        return True