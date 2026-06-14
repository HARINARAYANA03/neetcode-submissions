class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        d1_s_to_t={}
        d2_t_to_s={}
        
        for i in range(len(s)):
            
            char_s=s[i]
            char_t=t[i]
            
            if char_s in d1_s_to_t and d1_s_to_t[char_s]!=char_t:
                return False
            else:
                d1_s_to_t[char_s]=char_t
            
            
            if char_t in d2_t_to_s and d2_t_to_s[char_t]!=char_s:
                return False
            else:
                d2_t_to_s[char_t]=char_s
        return True