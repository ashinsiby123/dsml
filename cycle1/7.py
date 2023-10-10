def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num


print("Register no:SJC22MCA-2014")
print("Name       :Ashin Siby")
print("Batch      :2022-2024")
print("------------------------")

print("Armstrong numbers up to 1000:")
for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num)
