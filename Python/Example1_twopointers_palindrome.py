def check_palindrome(s: str):
    left = 0
    right = len(s) - 1

    while(left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

s = "racecar"
s1 = "hello"

print(check_palindrome(s))  # Output: True
print(check_palindrome(s1))  # Output: False