def is_perfect_number(num):
    if num <= 0:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num
try:
    print("Register no:SJC22MCA-2014")
    print("Name       :Ashin Siby")
    print("Batch      :2022-2024")
    print("------------------------")
    num = int(input("Enter a number: "))
    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")