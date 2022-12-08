#fibonacci series
def Fibonacci(n):
   
    if n ==0:
        return 0
    elif n==1 or n==2:
        
        return 1

    n=Fibonacci(n-1)+Fibonacci(n-2)
    return n


n=7
    
for i in range(n+1):
    print(Fibonacci(i))
    
