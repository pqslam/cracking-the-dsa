"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

"""
Assume that the 0 degree will be in the North side, to rotate the matrix 90 degrees, we rotate it to the East side
Example:
[1 2 3]      [7 4 1]
[4 5 6]  ->  [8 5 2]
[7 8 9]      [9 6 3]

[a b c d]    [m i e a]
[e f g h] -> [n j f b]
[i j k l]    [o k g c]
[m n o p]    [p l h d]

[00 01 02 03]     [30 20 10 00]
[10 11 12 13] ->  [31 21 11 01]
[20 21 22 23]     [32 22 12 02]
[30 31 32 33]     [33 23 13 03]

So, the first row will become the last column ; the last row will be come the first column.
"""

"Let's try with an easy solution without thinking about optimization"

"Time Complexity: O(N^2) where N is the number of elements in the matrix"
"Space Complexity: O(N) where N is the number of elements in the matrix, since we are creating a new matrix to store the rotated result"
def rotate_90_degrees(matrix: list) -> list:
    rotated_matrix = list()
    for col_idx in range(0,len(matrix)):
        temp_list = list()
        for row_idx in range(len(matrix)-1,-1,-1):
            temp_list.append(matrix[row_idx][col_idx])
        rotated_matrix.append(temp_list)
    return rotated_matrix


def rotate_90_degrees_in_place(matrix: list) -> None:
    #Rotate from layer to layer. We have N*N matrix => N layer
    matrix_length = len(matrix)
    for layer in range(0, matrix_length//2):
        for idx in range(layer, matrix_length - layer - 1):
        #save top for the last rotate
            temp = matrix[layer][matrix_length - idx - 1]
        #rotate left -> top
            matrix[layer][matrix_length - idx -1] = matrix[idx][layer]
        #rotate bottom -> left
            matrix[idx][layer] = matrix[matrix_length-layer - 1][idx]
        #rotate right -> bottom
            matrix[matrix_length-layer - 1][idx] = matrix[matrix_length - idx - 1][matrix_length - layer - 1]
        #rotate top (temp) -> right
            matrix[matrix_length - idx - 1][matrix_length - layer - 1] = temp

# Test the function
# if __name__ == "__main__":
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     print("Original Matrix:")
#     for row in matrix:
#         print(row)
    
#     rotated = rotate_90_degrees(matrix)
    
#     print("\nRotated Matrix:")
#     for row in rotated:
#         print(row)

#Test cases including edge cases
# ...existing code...

def test_rotate_functions():
    test_cases = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ],
            [
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]
            ]
        ),
        (
            [[42]],
            [[42]]
        ),
        (
            [],
            []
        ),
        (
            [
                ['a', 'b', 'c', 'd'],
                ['e', 'f', 'g', 'h'],
                ['i', 'j', 'k', 'l'],
                ['m', 'n', 'o', 'p']
            ],
            [
                ['m', 'i', 'e', 'a'],
                ['n', 'j', 'f', 'b'],
                ['o', 'k', 'g', 'c'],
                ['p', 'l', 'h', 'd']
            ]
        )
    ]

    for idx, (matrix, expected) in enumerate(test_cases):
        # Test rotate_90_degrees (returns new matrix)
        result = rotate_90_degrees(matrix)
        assert result == expected, f"rotate_90_degrees failed on test case {idx+1}"

        # Test rotate_90_degrees_in_place (modifies in place)
        # Only test in-place for non-empty, square matrices
        if matrix and len(matrix) == len(matrix[0]):
            import copy
            matrix_copy = copy.deepcopy(matrix)
            rotate_90_degrees_in_place(matrix_copy)
            assert matrix_copy == expected, f"rotate_90_degrees_in_place failed on test case {idx+1}"

    print("All test cases passed for both rotate_90_degrees and rotate_90_degrees_in_place!")

# Run the test cases
if __name__ == "__main__":
    test_rotate_functions()