#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, it's entire row and column are set to 0


def zeromatrix(matrix):




    #Done by self for MxN matrix
    row=len(matrix)
    column=len(matrix[0])
    hashlocation={}
    for i in range(row):
        for j in range(column):
            if(matrix[i][j]==0):
                hashlocation[i]=j
    for key,item in hashlocation.items():
        for i in range(row):
            matrix[i][item]=0
        for j in range(column):
            matrix[key][j]=0
    return matrix


matlist=[[ 1, 2, 3, 4],
         [ 5, 0, 7, 8],
         [ 9,10,11,1],]










#Done by self for NxN matrix
#     hashlocation={}
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if(matrix[i][j]==0):
#                 hashlocation[i]=j
                
                
#     for key,item in hashlocation.items():
#         for i in range(len(matrix)):
#             matrix[key][i]=0
#             matrix[i][item]=0    
#     return matrix
        

# matlist=[[ 1, 2, 3, 4],
#          [ 5, 0, 7, 8],
#          [ 9,10,11,0],
#          [13,14,15,16]]




print(zeromatrix(matlist))