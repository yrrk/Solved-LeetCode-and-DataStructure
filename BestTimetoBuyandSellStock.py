class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftpointer=0
        rightpointer=1
        profit=0
        while(rightpointer<len(prices)):
            if(profit<prices[rightpointer]-prices[leftpointer]):
                profit=prices[rightpointer]-prices[leftpointer]
                rightpointer+=1
            elif(prices[leftpointer]>prices[rightpointer]):
                leftpointer+=1
            else:
                rightpointer+=1   
        return profit
            