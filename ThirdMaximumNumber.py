class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=list(set(nums))
        num.sort()
        if(len(num)<=2):
            return num[-1]
        return num[-3]