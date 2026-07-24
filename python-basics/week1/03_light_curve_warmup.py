"""
Week 1 · Exercise 3 — A taste of the real project (transit-detection warmup)

A light curve is just a list of brightness measurements. When a planet transits,
brightness DIPS. You'll write baby transit detection with plain Python.
Run it:  python3 03_light_curve_warmup.py
"""


def normalize(brightness):
    """Divide every value by the average of the list, so the baseline sits around
    1.0 and dips show up as values below 1.0.
    average = sum(brightness) / len(brightness)"""
    # TODO
    pass


def find_dips(normalized, threshold=0.99):
    """Return the INDICES where normalized brightness drops below threshold.
    Hint: loop with enumerate(normalized) to get index + value."""
    # TODO
    pass


def deepest_dip(normalized):
    """Return the index of the single lowest brightness value."""
    # TODO
    pass


if __name__ == "__main__":
    raw = [100.0, 100.0, 100.0, 92.0, 100.0, 100.0]
    norm = normalize(raw)
    assert abs(sum(norm) / len(norm) - 1.0) < 1e-9
    assert find_dips(norm, threshold=0.99) == [3]
    assert deepest_dip(norm) == 3
    print("Exercise 3: all tests passed ✅  (you just wrote baby transit detection)")
