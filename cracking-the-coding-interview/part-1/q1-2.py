"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

"Time complexity: O(n) where n is the length of the input strings"
"Space complexity: O(n) since we are using a dictionary to store characters"
def check_permutation(str1: str, str2: str) -> bool:

    if len(str1) != len(str2):
        return False
    
    str1_dict = {}
    for char in str1:
        str1_dict[char] = str1_dict.get(char,0) + 1

    for char in str2:
        if  char not in str1_dict:
            return False
        str1_dict[char] -= 1
        if str1_dict[char] < 0:
            return False
    return True

"Test cases including edge cases"
def run_tests(func):
    assert func("abc", "cba") == True
    assert func("abc", "def") == False
    assert func("aabbcc", "abcabc") == True
    assert func("aabbcc", "abccba") == True
    assert func("", "") == True
    assert func("a", "a") == True
    assert func("a", "b") == False
    assert func("abc", "abcd") == False
    assert func("abcde", "edcba") == True
    assert func("12345", "54321") == True
    print(f"All test cases for {func.__name__} passed!")

if __name__ == "__main__":
    run_tests(check_permutation)
    print("Function is working correctly.")
