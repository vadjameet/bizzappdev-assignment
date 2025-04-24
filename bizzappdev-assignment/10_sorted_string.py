"""
Problem: Separate and Sort Letters/Digits
Approach: Use list comprehensions and sorted().
"""
def sort_string(s):
    letters = sorted([c for c in s if c.isalpha()])
    digits = sorted([c for c in s if c.isdigit()])
    return ''.join(letters + digits)

print(sort_string("B4A1D3"))  