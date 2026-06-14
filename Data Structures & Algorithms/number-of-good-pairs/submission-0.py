class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for value in freq.values():
            c+=value * (value-1) // 2
        return c