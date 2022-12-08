num = 2
arr = [1,2,4,11,12,8]

def DoubleSize(arr,b):
    l=len(arr)
    cs=set()
    for i in range(l):
        cs.add(arr[i])
    while b in cs:
        b=b*2
    return b


  






print(DoubleSize(arr,num))


range(len(arr))



# def findValue(a, n, k):
     
#     # Unordered Map
#     cs = set()
   
#     # Iterate from 0 to n - 1
#     for i in range(n):
#         m.add(a[i])
 
#     while (k in m):
#         k = k * 2
 
#     return k
 
# # Driver's Code
# arr, k = [ 2, 3, 4, 10, 8, 1 ], 2
# n = len(arr)
# print(findValue(arr, n, k))