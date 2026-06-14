class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for let in s:
            freq[let]=freq.get(let,0)+1
        for let in t:
            freq[let]=freq.get(let,0)-1
        for i in freq.values():
            if i!=0:
                return False
        return True