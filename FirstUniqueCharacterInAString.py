class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtab={}
        index=0
        for i in s:
            if(i in hashtab.keys()):
                hashtab[i]+=1
                continue
            hashtab[i]=1
        for i in s:
            if(hashtab[i]==1):
                return index
            index+=1
        return -1
    
        
        