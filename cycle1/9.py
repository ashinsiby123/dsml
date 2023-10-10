def add_lists(list1, list2):

    if len(list1) != len(list2):
        return None

    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result

try:
    print("Register no:SJC22MCA-2014")
    print("Name       :Ashin Siby")
    print("Batch      :2022-2024")
    print("------------------------")
    list1 = input("Enter the first list of numbers separated by spaces: ").split()
    list1 = [int(x) for x in list1]

    list2 = input("Enter the second list of numbers separated by spaces: ").split()
    list2 = [int(x) for x in list2]

    result = add_lists(list1, list2)

    if result is None:
        print("The lists have different lengths and cannot be added.")
    else:
        print("Result of addition:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")