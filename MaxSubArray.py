class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxSum=nums[0]
        curSum=0
        for i in range(n):
            curSum=curSum+nums[i]
            if(curSum>maxSum):
                maxSum=curSum
            if(curSum<0):
                curSum=0
        return maxSum