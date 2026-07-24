"""
Problem 1: Two Sum  (Easy) — WORKED EXAMPLE (your template)
https://leetcode.com/problems/two-sum/

Return the indices of the two numbers that add up to target.

--- APPROACH (written BEFORE coding) ---
Brute force = two nested loops, O(n^2). Better: walk once, keep a dict of
{value_seen: index}. For each number, the value I NEED is (target - number). If
that's already in the dict, I've found the pair. One pass, O(n).

--- WHAT TRIPPED ME UP ---
Instinct was nested loops. "Have I seen the complement?" is a lookup question,
and dicts make lookups instant.
"""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("two_sum: all tests passed ✅")
