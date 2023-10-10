def find_absent_digits(mobile_number):

    all_digits = set("0123456789")


    mobile_digits = set(mobile_number)


    absent_digits = all_digits - mobile_digits

    return sorted(list(absent_digits))


try:
    print("Register no:SJC22MCA-2014")
    print("Name       :Ashin Siby")
    print("Batch      :2022-2024")
    print("------------------------")
    mobile_number = input("Enter a 10-digit mobile number: ")

    if len(mobile_number) == 10 and mobile_number.isdigit():
        absent_digits = find_absent_digits(mobile_number)

        if absent_digits:
            print("Absent digits in the mobile number:", ', '.join(absent_digits))
        else:
            print("The mobile number contains all digits from 0 to 9.")
    else:
        print("Invalid input. Please enter a valid 10-digit mobile number.")
except ValueError:
    print("Invalid input. Please enter a valid 10-digit mobile number.")