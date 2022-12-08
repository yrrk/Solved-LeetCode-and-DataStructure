class Solution:
    def hammingWeight(self, n: int) -> int:
        bit=bin(n)[2:]
        counter=0
        for i in bit:
            if(i=='1'):
                counter+=1
        return counter
        