"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

"Time complexity: O(n^2) where n is the length of the input string"
"Space complexity: O(1) since we are not using any additional data structures"
def is_unique(input_string):
    is_unique = True
    for idx1 in range(0, len(input_string) - 1):
        for idx2 in range(idx1 + 1, len(input_string)):
            if input_string[idx1] == input_string[idx2] :
                is_unique = False
                break
            if not is_unique:
                break
    return is_unique

"Time complexity: O(n) where n is the length of the input string"
"Space complexity: O(n) since we are using a set to store unique characters"
def is_unique_with_set(input_string):
    is_unique = True
    input_set = set(input_string)
    if len(input_set) != len(input_string):
        is_unique = False
    return is_unique

"Time complexity: O(n) where n is the length of the input string"
"Space complexity: O(1) since we are using a fixed-size array to track characters"
def is_unique_optimal(input_string):
    if len(input_string) > 128:
        return False
    
    check_arr = [False] * 128
    for char in input_string:
        ascii_val = ord(char)
        if check_arr[ascii_val]:
            return False
        check_arr[ascii_val] = True
    return True

# Test cases including edge cases
def run_tests(func):
    assert func("abcdefg") == True
    assert func("abcdeafg") == False
    assert func("") == True
    assert func("a") == True
    assert func("ab") == True
    assert func("aa") == False
    assert func("abcABC") == True
    assert func("1234567890") == True
    assert func("1234567890a") == True
    assert func("!@#$%^&*()") == True
    assert func("!@#$%^&*()!") == False
    assert func("abcdefghijklmnopqrstuvwxyz") == True
    assert func("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == False
    assert func("a" * 1000) == False  # Large input with duplicates
    assert func("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
    assert func("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == False
    print(f"All test cases for {func.__name__} passed!")



if __name__ == "__main__":
    run_tests(is_unique)
    run_tests(is_unique_with_set)
    run_tests(is_unique_optimal)
    print("Functions are working correctly.")

        

