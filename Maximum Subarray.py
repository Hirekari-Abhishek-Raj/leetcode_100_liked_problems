class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=nums[0]
        curr=0
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            maxx=max(maxx,curr)
        return maxx
            
