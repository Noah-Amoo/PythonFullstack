# 1) Write a function that takes a list of numbers and returns a dictionary with keys: mean, median, mode, min, max — without using any statistics library.

def calculate_statistics(numbers):
    if not numbers:
        raise ValueError("The list is empty. Add numbers")
    
    #The sorted function orders the list from smallest to biggest
    sorted_numbers = sorted(numbers)
    count = len(numbers)

    # Calculating the mean: sum of all numbers divided by count of numbers
    mean = sum(numbers) / count

    # Calculating the mode
    if count % 2 == 1:
        median = sorted_numbers[count // 2]     # When count is odd

    middle1 = sorted_numbers[count // 2 - 1]
    middle2 = sorted_numbers[count // 2]
    median = (middle1 + middle2) / 2            # When count is even

    # Checking the mode or most frequent number
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_frequency = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_frequency]

    if modes == 1:
        mode = 0
    mode = modes

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "min": min(numbers),
        "max": max(numbers),
    }


# The following list will outputed the results below:
nums = [4, 2, 7, 2, 9, 4, 4]
print(calculate_statistics(nums))

# Output:   {'mean': 4.571428571428571, 'median': 4.0, 'mode': [4], 'min': 2, 'max': 9}



# 2) Implement a simple todo list program using a list. Support: add item, remove item by index, mark as done, display all items with status, and filter by done/pending.

def add_item(todo_list, item):
    todo_list.append({"task": item, "done": False})

def remove_item(todo_list, index):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
    else:
        raise ValueError("Index is not valid")

def mark_as_done(todo_list, index):
    if 0 <= index < len(todo_list):
        todo_list[index]["done"] = True
    else:
        raise ValueError("Invalid index")

def display_items(todo_list):
    if not todo_list:
        print("Todo list is empty")
        return
    
    for i, item in enumerate(todo_list):
        status = "Done" if item["done"] else "Pending"
        print(f"{i}. {item['task']} - {status}")


def filter_items(todo_list, status):
    if status == "done":
        filtered = [item for item in todo_list if item["done"]]

    elif status == "pending":
        filtered = [item for item in todo_list if not item["done"]]
    
    else:
        print("Mark as either 'done' or 'pending'.")
        return
    
    if not filtered:
        print("No matching items.")
        return
    
    for i, item in enumerate(filtered):
        print(f"{i}. {item['task']} - {'Done' if item['done'] else 'Pending'}")


# Example usage
todo_list = []

add_item(todo_list, "Complete Assignments")
add_item(todo_list, "Study Python")
add_item(todo_list, "Study Multithreading")

mark_as_done(todo_list, 1)
remove_item(todo_list, 0)

print("All items:")
display_items(todo_list)

print("\nDone items:")
filter_items(todo_list, "done")

print("\nPending items:")
filter_items(todo_list, "pending")

"""
Gives the following Output:

All items:
0. Study Python - Done
1. Study Multithreading - Pending

Done items:
0. Study Python - Done

Pending items:
0. Study Multithreading - Pending
"""


# 3) Write a program that generates the first N numbers of the Fibonacci sequence using both a for loop and a while loop. Compare the readability.

def fibonacci_for(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return sequence

def fibonacci_while(n):
    sequence = []
    a, b = 0, 1
    count = 0

    while count < n:
        sequence.append(a)
        a, b = b, a + b
        count += 1

    return sequence

n = 10
print("For loop:", fibonacci_for(n))
print("While loop:", fibonacci_while(n))

# In terms of readability, fibonnaci_ is clearer than fibonacci_for because the counter does not need any manual tuning