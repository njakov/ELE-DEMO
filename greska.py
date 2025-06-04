def calculate_average(numbers):
    total = 0
    for num in numbers: #Typo fixed
        total += num
    average = total / len(numbers)
    return average  # Typo fixed

nums = [10, 20, 30, 40, 50]
print("The average is:", calculate_average(nums))
