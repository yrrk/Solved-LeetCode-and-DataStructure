class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        lisy=[]
        lisy2=[]
        for i in x:
            lisy2.append(i)
        for i in x[::-1]:
            lisy.append(i)
        if(lisy==lisy2):
            return True
        else:
            return False