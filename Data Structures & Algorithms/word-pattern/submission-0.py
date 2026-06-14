class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        d1={}
        d2={}
        for i in range(len(pattern)):
            cp=pattern[i]
            cs=s[i]
            if cp in d1 and d1[cp]!=cs:
                return False
            if cs in d2 and d2[cs]!=cp:
                return False
            d1[cp]=cs
            d2[cs]=cp
        return True