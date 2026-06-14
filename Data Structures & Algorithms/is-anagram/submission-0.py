class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        freq1={}
        for let in s:
            freq[let]=freq.get(let,0)+1
        for lett in t:
            freq1[lett]=freq1.get(lett,0)+1
        return freq==freq1