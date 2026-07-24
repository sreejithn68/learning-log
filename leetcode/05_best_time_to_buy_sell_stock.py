"""
Problem 5: Best Time to Buy and Sell Stock  (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
prices[i] = price on day i. Buy one day, sell a later day. Return max profit, or 0.

--- MY APPROACH (write BEFORE coding) ---
TODO:
--- WHAT I GOT STUCK ON (after) ---
TODO:

Hint (only after 20 min): don't compare every pair. Walk once, tracking the
lowest price seen so far. Best profit if you sold today = today - lowest_so_far.
Keep the max of those.
"""


def max_profit(prices):
    # TODO
    pass


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1]) == 0
    print("max_profit: all tests passed ✅")
