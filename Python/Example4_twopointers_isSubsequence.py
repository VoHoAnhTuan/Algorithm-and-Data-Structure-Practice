def isSubsequence(s: str, t: str) -> bool:
    i = j = 0

    # "Iterate until one of the pointers reaches the end of its respective string."
    # "If the characters at the pointers are equal, move the pointer of s one step to the right."
    # "Always move the pointer of t one step to the right."
    # "If we reach this point, it means all characters of s are found in t in order, so return True."
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1 # Always increment j

    return i ==len(s)

# Example usage
s = "abc"
t = "ahbgdc"
s1 = "axc"
t1 = "ahbgdc"
print(isSubsequence(s, t))  # Output: True
print(isSubsequence(s1, t1))  # Output: False
