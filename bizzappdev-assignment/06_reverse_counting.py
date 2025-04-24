"""
Problem: Reverse Counting using Recursion
Approach: Recursive function with base case at 1.
"""
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n-1)

# Start from 1000
countdown(1000)