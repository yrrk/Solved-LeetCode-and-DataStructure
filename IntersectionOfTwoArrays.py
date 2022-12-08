class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        interlist=[]
        for i in range(len(nums1)):
            if(nums1[i] in hashmap.keys()):
                hashmap[nums1[i]]+=1
                continue
            hashmap[nums1[i]]=1
        print(hashmap)
        
        for i in nums2:
            if(i in hashmap.keys() and hashmap[i]!=0):
                interlist.append(i)
                hashmap[i]-=1
        return interlist
                
        