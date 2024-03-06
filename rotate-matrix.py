# Problem: Rotate given matrix by 90 Degrees


martix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

martix2 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]


def rotateMatrixTranspose(matrix):
    # Transpose the matrix first
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row = row[::-1]
        print(row)


def rotateMatrixLayerwise(matrix):
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right-left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom-i][left] = matrix[bottom][right - i]
            matrix[bottom][right-i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft
        left+=1
        right-=1
    for row in matrix:
        print(row)


rotateMatrixTranspose(martix1.copy())
print("\n")
rotateMatrixTranspose(martix2.copy())
print("\n")
rotateMatrixLayerwise(martix1.copy())
print("\n")
rotateMatrixLayerwise(martix2.copy())
