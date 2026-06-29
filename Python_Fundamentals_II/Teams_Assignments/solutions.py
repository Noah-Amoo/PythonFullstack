def total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]

    return total

def spent_by_category(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories


def biggest_expense(expenses):
    biggest = expenses[0]

    for expense in expenses:
        if expense["amount"] > biggest["amount"]:
            biggest = expense

    return biggest


# Testing the Functions
expenses = [
    {"name": "Groceries", "category": "Food", "amount": 45.0},
    {"name": "Bus pass", "category": "Transport", "amount": 30.0},
    {"name": "Dinner", "category": "Food", "amount": 25.0},
    {"name": "Taxi", "category": "Transport", "amount": 15.0},
]

print(total_expense(expenses))
print(spent_by_category(expenses))
print(biggest_expense(expenses))

"""
The above produced the following output
115.0
{'Food': 70.0, 'Transport': 45.0}
{'name': 'Groceries', 'category': 'Food', 'amount': 45.0}
"""