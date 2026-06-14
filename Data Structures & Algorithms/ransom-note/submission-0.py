class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        for i in magazine:
            d1[i]=d1.get(i,0)+1
        for i in ransomNote:
            d1[i]=d1.get(i,0)-1
            if d1[i]<0:
                return False
        return True