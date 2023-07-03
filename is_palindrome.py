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