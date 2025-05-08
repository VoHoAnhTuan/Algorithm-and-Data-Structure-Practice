# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse_string(s: list[str]):
    i = 0
    j = len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

        """# Traditional swapping with a temporary variable
            temp = s[i]
            s[i] = s[j]
            s[j] = temp"""

# Example usage
s = ["h", "e", "l", "l", "o"]
s1 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s)
reverse_string(s1)
print(s)  # Output: ["o", "l", "l", "e", "h"]
print(s1)  # Output: ["h", "a", "n", "n", "a", "H"]