def is_palindrome(input_string):
    # return input_string == input_string[::-1]  ## simple way to do it

    # Algorithmic way
    start = 0
    end = len(input_string)-1

    while input_string[start] == input_string[end]:
        if start > end//2:
            return True
        start +=1
        end -= 1
    return False
print(is_palindrome("saippuakivikauppias")) # True
print(is_palindrome("apples")) # False

def is_anagram(str1, str2):
    dict1 = {}
    dict2 = {}

    for char in str1:
        char = char.lower()
        dict1[char] = dict1.get(char, 0) + 1
        
    for char in str2:
        char = char.lower()
        dict2[char] = dict2.get(char, 0) + 1

    return dict1 == dict2

print(is_anagram("angel", "glean")) # True
print(is_anagram("angel", "GLEAN")) # True
print(is_anagram("angel", "gleann")) # False
print(is_anagram("Pickles", "Eggplant")) # False


def is_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_string = input_string.lower()

    for char in alphabet:
        if char not in input_string:
            return False

    return True
print(is_pangram("A quick brown fox jumps over the")) # False
print(is_pangram("A quick brown fox jumps over the lazy dog")) # True