# Assignment 2 — Bank Account Class

**Topic:** writing a class (OOP). **Required.**

## Task
Write a `BankAccount` class with:

- a constructor taking an `owner` name and a starting `balance` (default `0`),
- `deposit(amount)` — adds money,
- `withdraw(amount)` — removes money, but raises an error if there isn't enough,
- a `balance` you can read at any time.

Rules:
- Depositing or withdrawing zero/negative money should raise `ValueError`.
- Withdrawing more than the balance should raise an error (make your own
  `InsufficientFundsError`).

## Example usage and output
```python
acc = BankAccount("Zara", 100.0)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance)     # -> 120.0

acc.withdraw(1000)     # -> raises InsufficientFundsError
```

## Done when
- [ ] The example above prints `120.0`.
- [ ] Over-withdrawing raises your custom error.
- [ ] Zero/negative amounts raise `ValueError`.
