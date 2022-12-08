class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target in nums):
            return nums.index(target)
        else:
            for i in nums:
                if(i>target):
                    insind=nums.index(i)
                    break
                if(i==nums[-1] and target>i):
                    insind=nums.index(i)+1    
            return insind