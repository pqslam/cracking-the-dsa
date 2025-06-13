"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

"Time Complexity: O(M * N) where M is the number of rows and N is the number of columns in the matrix."
"Space Complexity: O(M + N) where M is the number of rows and N is the number of columns in the matrix, since we are storing the indices of zero rows and columns."
def make_zero_matrix(matrix: list, num_rows, num_cols) -> None:
    zero_column_idxes = list()
    zero_row_idxes = list()

    for row_idx in range(0, num_rows):
        for col_idx in range(0, num_cols):
            if matrix[row_idx][col_idx] == 0:
                zero_row_idxes.append(row_idx)
                zero_column_idxes.append(col_idx)

    for row_idx in zero_row_idxes:
        matrix[row_idx] = [0] * num_cols
    
    for col_idx in zero_column_idxes:
        for row_idx in range(0, num_rows):
            matrix[row_idx][col_idx] = 0


"""
[x][0][x][x]
[x][x][x][x]
[x][x][0][x]
[x][x][x][0]

Find the first 0 and create markers
|x||0||x||x|
[x]|x|[x][x]
[x]|x|[0][x]
[x]|x|[x][0]

Update the market when meeting the next 0
After all, the matrix should be like
|x||0||0||0|
[x]|x|[x][x]
[x]|0|[0][x]
[x]|0|[x][0]

Use the markers to update the whole matrix 
|0||0||0||0|
[x]|0|[0][0]
[0]|0|[0][0]
[0]|0|[0][0]
"""
def make_zero_matrix_optimal(matrix: list, num_rows, num_cols) -> None:
    zero_column_marker = None
    zero_row_marker = None

    for row_idx in range(0, num_rows):
        for col_idx in range(0, num_cols):
            if matrix[row_idx][col_idx] == 0:
                if zero_column_marker == None:
                    zero_column_marker = col_idx
                if zero_row_marker == None:
                    zero_row_marker = row_idx
                matrix[row_idx][zero_column_marker] = 0
                matrix[zero_row_marker][col_idx] = 0

    if zero_row_marker != None:
        for row_idx in range(0, num_rows):
            if row_idx != zero_row_marker and matrix[row_idx][zero_column_marker] == 0:
                matrix[row_idx] = [0] * num_cols
        for col_idx in range(0, num_cols):
            if matrix[zero_row_marker][col_idx] == 0:
                for row_idx in range(0, num_rows):
                    matrix[row_idx][col_idx] = 0
        matrix[zero_row_marker] = [0] * num_cols
            


# Test cases including edge cases
def test_make_zero_matrix():
    test_cases = [
        (
            [
                [1, 2, 3],
                [4, 0, 6],
                [7, 8, 9]
            ],
            [
                [1, 0, 3],
                [0, 0, 0],
                [7, 0, 9]
            ]
        ),
        (
            [
                [1, 2],
                [3, 4]
            ],
            [
                [1, 2],
                [3, 4]
            ]
        ),
        (
            [
                [0]
            ],
            [
                [0]
            ]
        ),
        (
            [
                [1, 2],
                [0, 4]
            ],
            [
                [0, 2],
                [0, 0]
            ]
        ),
        (
            [
                [1, 0, 3],
                [4, 5, 6],
                [7, 8, 0]
            ],
            [
                [0, 0, 0],
                [4, 0, 0],
                [0, 0, 0]
            ]
        )
    ]

    for i, (input_matrix, expected_output) in enumerate(test_cases):
        make_zero_matrix_optimal(input_matrix, len(input_matrix), len(input_matrix[0]))
        assert input_matrix == expected_output, f"Test case {i+1} failed"
    print("All test cases passed!") 

# Run the test cases
if __name__ == "__main__":
    test_make_zero_matrix()
    print("All test cases passed for make_zero_matrix!")