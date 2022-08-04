def matrix_subtraction(matrix1, matrix2):
    sum = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    result = [matrix1, matrix2]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum[i][j] = matrix1[i][j] - matrix2[i][j]
    for k in range(2):
        print(f"Matrix {k+1}:")
        for l in range(len(sum)):
            print(f"{result[k][l]}")
    print("The result matrix is:")
    for d in sum:
        print(d)


matrix_subtraction([[10,5,4,2],[5,10,9,55],[9,19,69,8],[7,8,4,75]],[[12,65,34,2],[1,5,8,45],[7,21,63,8],[0,78,4,65]])