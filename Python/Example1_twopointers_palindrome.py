def check_palindrome(s: str):
    # "Set the starting and ending pointers to the first and last characters of the string."
    left = 0
    right = len(s) - 1

    # "Iterate until the left pointer is less than the right pointer, which means we have checked all characters."
    #  "If the characters at the left and right pointers are not equal, return False."
    #  "If they are equal, move the left pointer one step to the right and the right pointer one step to the left."
    #  "If we reach this point, it means the string is a palindrome, so return True."

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

s = "racecar"
s1 = "hello"

print(check_palindrome(s))  # Output: True
print(check_palindrome(s1))  # Output: False