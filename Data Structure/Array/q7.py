#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes.
#Write a method to rotate the image by 90 degrees. Can you do this in place?



def rotate_matrix(matrix):
    n=len(matrix)
    
    for i in range(n):
        for j in range(i,n):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp

    for i in range(n):
        matrix[i].reverse()
        
    return matrix

matlist=[[ 1, 2, 3, 4],
         [ 5, 6, 7, 8],
         [ 9,10,11,12],
         [13,14,15,16],]

print(rotate_matrix(matlist))