def matrix_addition(matrix1, matrix2):
    sum = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            sum[i][j] = matrix1[i][j] + matrix2[i][j]
    for k in sum:
        print(k)


matrix_addition([[10,5,4,2],[5,0,9,5],[9,19,60,8],[7,8,4,5]],[[12,65,34,42],[10,5,89,45],[11,21,63,78],[87,78,54,65]])