def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (potential error case):
my_numbers = [10, 20, 30, 0]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")