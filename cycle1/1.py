lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))
print("Register no:SJC22MCA-2014")
print("Name       :Ashin Siby")
print("Batch      :2022-2024")
print("------------------------")
print("The Non-Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
    if number <= 1:
        # Numbers less than or equal to 1 are not prime.
        print(number)
    else:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                # If the number is divisible by any integer other than 1 and itself, it's not prime.
                is_prime = False
                break
        if not is_prime:
            print(number)
