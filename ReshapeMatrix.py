class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        samplelist=[]
        outputlist=[]
        for i in mat:
            for j in i:
                samplelist.append(j)
        k=0   
        if(r*c==len(samplelist)):
            while(k<r):
                row=[]
                for i in range(c):
                    row.append(samplelist.pop(0))
                outputlist.append(row)
                k+=1
            return outputlist
        else:
            return mat