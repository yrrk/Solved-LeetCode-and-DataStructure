n = ['ball', 'box', 'ball', 'ball', 'box']
p = [2 , 2 , 2 , 2 , 2]
w = [1, 2, 1, 1, 3]

def numDuplicates(name,price,weight):
    hasht=set()
    item=[]
    cnt=0
    for i in range(len(name)):
        item.append(name[i])
        item.append(price[i])
        item.append(weight[i])
        if(tuple(item) in hasht):
            cnt+=1
            item=[]
            continue
        hasht.add(tuple(item))
        item=[]
    return cnt


print(numDuplicates(n,p,w))




