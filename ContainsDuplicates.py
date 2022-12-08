class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashT={}
        for i in nums:
            if(i in hashT.keys()):
                return True
            else:
                hashT[i]=False
        return False