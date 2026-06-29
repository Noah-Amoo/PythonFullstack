# Assignment 1 — Expense Summary

**Topic:** lists, dictionaries, functions. **Required.**

## Task
You are given a list of expenses. Each expense is a dictionary with a `name`,
a `category`, and an `amount`. Write three functions:

1. `total_spent(expenses)` — the total of all amounts.
2. `spend_by_category(expenses)` — a dictionary of category → total for that category.
3. `biggest_expense(expenses)` — the single expense dictionary with the largest amount.

## Example input
```python
expenses = [
    {"name": "Groceries", "category": "Food", "amount": 45.0},
    {"name": "Bus pass", "category": "Transport", "amount": 30.0},
    {"name": "Dinner", "category": "Food", "amount": 25.0},
    {"name": "Taxi", "category": "Transport", "amount": 15.0},
]
```

## Example output
```
total_spent(expenses)        -> 115.0
spend_by_category(expenses)  -> {"Food": 70.0, "Transport": 45.0}
biggest_expense(expenses)    -> {"name": "Groceries", "category": "Food", "amount": 45.0}
```

## Done when
- [ ] All three functions return the values shown above.
- [ ] You used a loop or comprehension, not hard-coded numbers.
