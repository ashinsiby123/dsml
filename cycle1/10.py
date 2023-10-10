def add_matrices(matrix1, matrix2):

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None


    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

try:
    print("Register no:SJC22MCA-2014")
    print("Name       :Ashin Siby")
    print("Batch      :2022-2024")
    print("------------------------")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter elements of the first matrix:")
    matrix1 = []
    for i in range(rows):
        row = input(f"Enter elements of row {i + 1} separated by spaces: ").split()
        matrix1.append([int(x) for x in row])

    print("Enter elements of the second matrix:")
    matrix2 = []
    for i in range(rows):
        row = input(f"Enter elements of row {i + 1} separated by spaces: ").split()
        matrix2.append([int(x) for x in row])


    result = add_matrices(matrix1, matrix2)

    if result is None:
        print("Matrix dimensions are not compatible for addition.")
    else:
        print("Sum of matrices:")
        for row in result:
            print(" ".join(map(str, row)))
except ValueError:
    print("Invalid input. Please enter valid numbers.")