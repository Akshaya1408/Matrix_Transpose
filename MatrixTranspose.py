def matrixTranspose(matrix,rows,columns):

    column=len(matrix[0])
    tran = [[0 for i in range(rows)] for j in range(column)]

    for i in range(rows):
        for j in range(column):
            tran[j][i] = matrix[i][j]

    return tran

matrix=[]
rows=int(input("No of rows : "))
columns=int(input("No of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))

print(matrixTranspose(matrix,rows,columns))