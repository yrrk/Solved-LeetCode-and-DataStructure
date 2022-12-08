# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        n1=1
        n2=2
        ways=0
        if(n>2):
            for i in range(n-2):
                ways=n1+n2
                n1=n2
                n2=ways
        elif(n==1):
            return 1
        else:
            return 2
        return ways