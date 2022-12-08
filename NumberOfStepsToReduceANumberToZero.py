class Solution:
    def numberOfSteps(self, num: int) -> int:
        a=0
        while num>0:
            if num%2==0:
                num=num/2
                a=a+1
            elif num==0:
                a=a+1
            else:
                num=num-1
                a=a+1
        return a     
                