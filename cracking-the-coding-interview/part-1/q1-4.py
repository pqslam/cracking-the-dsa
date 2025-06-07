"""
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

"Time complexity: O(n) where n is the length of the input string"
"Space complexity: O(1) since we are using a fixed-size dictionary (26 at most) to store character counts"
def check_palindrome_permutation(input: str) -> bool:
    input_dict = dict()
    char_count = 0
    for char in input:
        if char != " ":
            char_count += 1
            input_dict[char.lower()] = input_dict.get(char.lower(),0) + 1

    if char_count % 2 == 0:
        for key in input_dict:
            if input_dict[key] % 2 != 0:
                return False
    else:
        num_odd = 0
        for key in input_dict:
            if input_dict[key] % 2 != 0:
                num_odd += 1
                if num_odd > 1:
                    return False
    return True

# Test cases including edge cases
def run_tests(func):
    assert func("Tact Coa") == True
    assert func("taco cat") == True
    assert func("atco eta") == False
    assert func("abc") == False
    assert func("aabbcc") == True
    assert func("aabbccdd") == True
    assert func("aabbccdde") == True
    assert func("aabbccddeee") == True
    assert func("a") == True
    assert func("aa") == True
    assert func("ab") == False
    assert func("abcba") == True
    assert func("abcde") == False
    print(f"All test cases for {func.__name__} passed!")

if __name__ == "__main__":
    run_tests(check_palindrome_permutation)
    print("Function is working correctly.")
        