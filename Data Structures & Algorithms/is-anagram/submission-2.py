class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=list(s)        
        list2=list(t)
        list1.sort()
        list2.sort()
        q="".join(list1)
        w="".join(list2)
        return q==w