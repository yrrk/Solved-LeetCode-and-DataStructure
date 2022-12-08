class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row=0
        outputlist=[]
        if(row==0 and row<numRows):
            outputlist.append([1])
            row+=1
        if(row==1 and row<numRows):
            outputlist.append([1,1])
            row+=1
        
        
        while(row<numRows):
            i=0
            rowlist=[]
            if(i==0):
                rowlist.append(1)
                i+=1
            while(i<len(outputlist[row-1])):
                rowlist.append(outputlist[row-1][i-1]+outputlist[row-1][i])
                i+=1
            rowlist.append(1)
            outputlist.append(rowlist)
            row+=1
        return outputlist