# Assignment 3 — Tidy Up a Messy Function

**Topic:** clean code (one function = one job, avoid long if/elif chains). **Required.**

## The messy code you start with
```python
def process_order(items, coupon):
    total = 0
    for it in items:
        total += it["price"] * it["qty"]
    if coupon == "SAVE10":
        total = total * 0.9
    elif coupon == "VIP":
        total = total * 0.8
    print("Total is", total)
    return total
```

## Task
Clean this up:
1. Split it into small functions, each doing **one** job
   (e.g. one to add up the items, one to apply the discount).
2. Replace the `if/elif` coupon chain with a **dictionary** of coupon → discount,
   so adding a new coupon means adding one line, not a new `if`.
3. Don't `print` inside the calculation — just return the number.

## Example input and output
```python
items = [{"price": 50, "qty": 2}, {"price": 20, "qty": 1}]

order_total(items)         # -> 120.0   (no coupon)
order_total(items, "VIP")  # -> 96.0    (20% off)
```

## Done when
- [ ] The work is split into small, clearly named functions.
- [ ] Coupons live in a dictionary, not an if/elif chain.
- [ ] Same totals as above; no printing inside the calculation.
