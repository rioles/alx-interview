#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    left, right = 0, len(matrix[0]) - 1

    while left < right:

        for i in range(right - left):
            top, bottom = left, right

            top_left = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left

        left += 1
        right -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ rotate_2d_matrix(matrix) """
    rotate_2d_matrix(matrix)
    print(matrix)
