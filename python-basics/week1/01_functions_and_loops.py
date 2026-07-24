"""
Week 1 · Exercise 1 — Functions, loops, and conditionals

Fill in each function so the tests at the bottom pass.
Run it:  python3 01_functions_and_loops.py
Struggle before looking anything up. Then write what tripped you up as a comment.
"""


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit. Formula: F = C * 9/5 + 32"""
    f = c * 9/5 + 32
    return f
    pass


def count_evens(numbers):
    """Return how many numbers in the list are even.
    Hint: a number is even if  number % 2 == 0."""
    iseven = 0
    for l in numbers:
      if l%2==0:
        iseven=iseven + 1
    return iseven
    pass


def largest(numbers):
    """Return the largest number WITHOUT using the built-in max().
    Hint: keep a 'best so far' variable and update it as you loop."""
     
    best = numbers [0]
    for n in numbers:
        if n > best:
            best = n
    return best
     
    pass


# --- Tests: run this file. Silence + ✅ means you passed. ---
if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert count_evens([1, 2, 3, 4, 5, 6]) == 3
    assert count_evens([]) == 0
    assert largest([3, 7, 2, 9, 4]) == 9
    assert largest([-5, -2, -10]) == -2
    print("Exercise 1: all tests passed ✅")
