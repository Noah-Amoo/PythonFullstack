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



