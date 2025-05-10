"""Example 2: You are given a binary string s (a string containing only "0" and "1").
You may choose up to one "0" and flip it to a "1".
What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5.
If you perform the flip at index 2, the string becomes 1111100111."""

def find_binary_string_max_length(s: str) -> int:
    left = 0
    current_zero_count = 0
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        if s[right] == '0':
            current_zero_count += 1

        # If we have more than one zero, move the left pointer to the right
        # until we have at most one zero in the window
        while current_zero_count > 1:
            if s[left] == '0':
                current_zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage
s = "1101100111"
result = find_binary_string_max_length(s)
print(result)  # Output: 5

