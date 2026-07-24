"""
Week 1 · Exercise 2 — Lists, dictionaries, and comprehensions
Run it:  python3 02_lists_and_dicts.py
"""


def squares(n):
    """Return [1, 4, 9, ...] the squares of 1..n. Try a list comprehension:
    [x * x for x in range(1, n + 1)]"""
    # TODO
    pass


def word_counts(words):
    """Given a list of words, return a dict mapping each word to how many times
    it appears. e.g. ['a','b','a'] -> {'a': 2, 'b': 1}
    Hint: loop, and use  counts[word] = counts.get(word, 0) + 1"""
    # TODO
    pass


def filter_above(numbers, threshold):
    """Return only the numbers strictly greater than threshold."""
    # TODO
    pass


if __name__ == "__main__":
    assert squares(4) == [1, 4, 9, 16]
    assert word_counts(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}
    assert word_counts([]) == {}
    assert filter_above([1.0, 5.5, 2.2, 9.9], 3.0) == [5.5, 9.9]
    print("Exercise 2: all tests passed ✅")
