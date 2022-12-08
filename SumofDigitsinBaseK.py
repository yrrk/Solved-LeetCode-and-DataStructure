class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum=0
        while(True):
            r=n//k
            s=n%k
            n=r
            sum=sum+s
            if(n==0):
                break
        return sum
        