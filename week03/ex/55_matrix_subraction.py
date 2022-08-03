def matrix_subraction(matrix1, matrix2):
    sum = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum[i][j] = matrix1[i][j] - matrix2[i][j]
    for k in sum:
        print(k)


matrix_subraction([[10,5,4,2],[5,10,9,55],[9,19,69,8],[7,8,4,75]],[[12,65,34,2],[1,5,8,45],[7,21,63,8],[0,78,4,65]])