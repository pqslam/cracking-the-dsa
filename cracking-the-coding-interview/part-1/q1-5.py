"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

def check_insert_remove(long_str: str, short_str: str) -> bool:
    compared_idx = 0
    for idx in range(0, len(short_str)):
        if short_str[idx] != long_str[compared_idx]:
            if compared_idx+1 < len(long_str) and short_str[idx] == long_str[compared_idx+1]:
                compared_idx += 1
            else:
                return False
        compared_idx +=1
    return True

"Time complexity: O(n), where n is the length of the longer string."
"Space complexity: O(1), no additional space is used that scales with input size."
def check_one_edit(str1 : str, str2: str) -> bool:
    # If the length difference is greater than 2 (need at least 2 edits), return false immediately
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    # Case replace a character
    is_one_edit = False
    if len(str1) == len(str2):
        for idx in range(0, len(str1)):
            if str1[idx] != str2[idx]:
                if is_one_edit: # if already have 1 edit needed -> False case
                    return False
                else:
                    is_one_edit = True
    # Case insert or remove a character
    elif len(str1) > len(str2):
        is_one_edit = check_insert_remove(str1, str2)
    else:
        is_one_edit = check_insert_remove(str2, str1)
    
    return is_one_edit
    
# Test cases including edge cases
def run_tests(func):
    assert func("pale", "ple") == True
    assert func("pale", "pli") == False
    assert func("pales", "pale") == True
    assert func("pale", "bale") == True
    assert func("pale", "bake") == False
    assert func("pale", "baae") == False
    assert func("abc", "ab") == True
    assert func("ab", "abc") == True
    assert func("a", "b") == True
    assert func("a", "") == True
    assert func("", "a") == True
    assert func("", "") == False
    print(f"All test cases for {func.__name__} passed!")

if __name__ == "__main__":
    run_tests(check_one_edit)
    print("Function is working correctly.")
