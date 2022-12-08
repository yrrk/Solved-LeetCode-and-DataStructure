#Google Question
#Array=[2,5,1,2,3,5,1,2,4]
#it should return 2
#Array=[2,1,1,2,3,5,1,2,4]
#it should return 1
#Array=[2,3,4,5]
#it should return undefined


ASrray=[2,3,4,5]
hasht={}
for i in ASrray:
    if(i in hasht.keys()):
        hasht[i]=True
        print(i)
        break
    else:
        hasht[i]=False
if True not in hasht.values():
    print(None)
