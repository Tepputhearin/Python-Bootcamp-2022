def matrix_multiplication(matrix1, matrix2):
    sum = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = [matrix1,matrix2]
    if len(matrix1[0]) != len(matrix2) or len(matrix1) != len(matrix2[0]):
        if len(matrix1) != len(matrix2):
            print("Error")
    else:
        for i in range(len(matrix1)):
            for j in range(len(matrix1)):
                for l in range(len(matrix1)):
                    sum[i][j] += matrix1[i][l] * matrix2[l][j]
        for k in range(2):
            print(f"Matrix {k+1}:")
            for l in range(len(sum)):
                print(f"{result[k][l]}")
        print("The result matrix is:")
        for d in sum:
            print(d)


matrix_multiplication([[3, 7, 5], [2, 6, 7], [4, 3, 2]], [[6, 5, 4], [3, 2, 1], [1, 2, 3]])