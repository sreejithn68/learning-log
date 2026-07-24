"""
Problem 2: Contains Duplicate  (Easy)
https://leetcode.com/problems/contains-duplicate/
Return True if any value appears at least twice, else False.

--- MY APPROACH (write BEFORE coding) ---
TODO:
--- WHAT I GOT STUCK ON (after) ---
TODO:

Hint (only after 20 min): a set stores unique items. Compare len(set(nums)) to
len(nums) — or build a set as you go and check membership before adding.
"""


def contains_duplicate(nums):
    # TODO
    pass


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    print("contains_duplicate: all tests passed ✅")
