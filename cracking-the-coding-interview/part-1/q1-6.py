"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def is_smaller_than_original(input: list) -> bool:
    min_length = 0
    count = 1
    for idx in range(1, len(input)):
        if input[idx] != input[idx-1]:
            min_length += 1 + len(str(count))
            count = 1
        else:
            count += 1
    min_length += 1 + len(str(count))
    if min_length >= len(input):
        return False
    else:
        return True
    
def insert_character_and_count(input: list, insert_idx: int, character: str, count: int) -> None:
    input[insert_idx] = character
    input[insert_idx + 1] = str(count)
"""
Need to keep track of:
- the current character -> count
- the index to insert character and count number
Modify the input when:
- current character changed
- at the end of the input (list)
"""

def compress_string(input: str) -> str:
    input = list(input)
    if not is_smaller_than_original(input):
        return ''.join(input)
    
    current_char = input[0]
    insert_idx = 0 # depend on count, it will increase by 2 or 3 or 4...
    char_count = 1
    for idx in range(1, len(input)):
        if input[idx] != current_char:
            temp = input[idx]
            insert_character_and_count(input, insert_idx, current_char, char_count)
            insert_idx += 1 + len(str(char_count))
            current_char = temp
            char_count = 1
        else:
            char_count += 1
    
    insert_character_and_count(input, insert_idx, current_char, char_count)
    insert_idx += 1 + len(str(char_count))
    
    return ''.join(input[:insert_idx])

            
# Test cases including edge cases
def run_tests(func):
    assert func("aabcccccaaa") == "a2b1c5a3"
    assert func("abc") == "abc"
    assert func("a") == "a"
    assert func("") == ""
    assert func("aa") == "aa"
    assert func("aaa") == "a3"
    assert func("aabbcc") == "aabbcc"
    assert func("aabbccddeeff") == "aabbccddeeff"
    assert func("aabbccddeeffgghh") == "aabbccddeeffgghh"
    assert func("aabbccddeeffggg") == "a2b2c2d2e2f2g3"
    assert func("aaaabbbbccddeeffgggh") == "a4b4c2d2e2f2g3h1"
    print(f"All test cases for {func.__name__} passed!")

if __name__ == "__main__":
    run_tests(compress_string)
    print("All tests passed successfully!")
