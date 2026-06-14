class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for i in magazine:
            d1[i]=d1.get(i,0)+1
        for i in ransomNote:
            d2[i]=d2.get(i,0)+1
        for i in d2:
            if d2[i]>d1.get(i,0):
                return False
        return True