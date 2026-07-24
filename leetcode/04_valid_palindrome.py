"""
Problem 4: Valid Palindrome  (Easy)
https://leetcode.com/problems/valid-palindrome/
After lowercasing and removing non-alphanumerics, does it read the same both ways?

--- MY APPROACH (write BEFORE coding) ---
TODO:
--- WHAT I GOT STUCK ON (after) ---
TODO:

Hint (only after 20 min): str methods .lower() and .isalnum(). Build a cleaned
string of only alphanumerics, then compare it to its reverse: cleaned == cleaned[::-1].
"""


def is_palindrome(s):
    # TODO
    pass


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    print("is_palindrome: all tests passed ✅")
