def matrix_addition(matrix1, matrix2):
    sum = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    result = [matrix1, matrix2]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            sum[i][j] = matrix1[i][j] + matrix2[i][j]
    for k in range(2):
        print(f"Matrix {k+1}:")
        for l in range(len(sum)):
            print(f"{result[k][l]}")
    print("The result matrix is:")
    for d in sum:
        print(d)



matrix_addition([[10,5,4,2],[5,0,9,5],[9,19,60,8],[7,8,4,5]],[[12,65,34,42],[10,5,89,45],[11,21,63,78],[87,78,54,65]])