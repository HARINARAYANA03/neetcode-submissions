class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mx=max(nums)
        mn=min(nums)
        freq=[0]*(mx-mn+1)
        for i in nums:
            freq[i-mn]+=1
        nums=[]
        for i in range(len(freq)):
            while freq[i]>0:
                nums.append(i+mn)
                freq[i]-=1
        return nums