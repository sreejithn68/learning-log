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
    average = sum(brightness)/ len(brightness)
    x = [b / average for b in brightness]
    return x
    pass


def find_dips(normalized, threshold=0.99):
    """Return the INDICES where normalized brightness drops below threshold.
    Hint: loop with enumerate(normalized) to get index + value."""
    result = []
    for i, value in enumerate (normalized):
        if value < threshold:
            result.append(i)
    return result    
    
pass


def deepest_dip(normalized):
    """Return the index of the single lowest brightness value."""
    best_index=0
    for i, value in enumerate (normalized):
        if value < normalized [best_index]:
             best_index = i
    return best_index    
    pass


if __name__ == "__main__":
    raw = [100.0, 100.0, 100.0, 92.0, 100.0, 100.0]
    norm = normalize(raw)
    assert abs(sum(norm) / len(norm) - 1.0) < 1e-9
    assert find_dips(norm, threshold=0.99) == [3]
    assert deepest_dip(norm) == 3
    print("Exercise 3: all tests passed ✅  (you just wrote baby transit detection)")
