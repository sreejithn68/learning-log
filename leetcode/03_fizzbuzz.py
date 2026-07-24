"""
Problem 3: Fizz Buzz  (Easy)
https://leetcode.com/problems/fizz-buzz/
Return a list of strings for 1..n:
  multiple of 3 and 5 -> "FizzBuzz"; of 3 -> "Fizz"; of 5 -> "Buzz"; else the number.

--- MY APPROACH (write BEFORE coding) ---
TODO:
--- WHAT I GOT STUCK ON (after) ---
TODO:

Hint (only after 20 min): % is remainder; n % 3 == 0 means divisible by 3.
Check the 3-AND-5 case FIRST — order matters.
"""


def fizz_buzz(n):
    # TODO
    pass


if __name__ == "__main__":
    assert fizz_buzz(3) == ["1", "2", "Fizz"]
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(15)[-1] == "FizzBuzz"
    print("fizz_buzz: all tests passed ✅")
