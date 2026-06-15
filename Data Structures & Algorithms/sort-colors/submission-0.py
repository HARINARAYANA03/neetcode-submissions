class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        freq=[0]*3
        for i in nums:
            freq[i]+=1
        index=0
        for i in range(3):
            while freq[i]>0:
                nums[index]=i
                index+=1
                freq[i]-=1