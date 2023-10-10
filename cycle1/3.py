def check_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


print("Register no:SJC22MCA-2014")
print("Name       :Ashin Siby")
print("Batch      :2022-2024")
print("------------------------")
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. Side lengths must be positive.")
else:
    triangle_type = check_triangle_type(a, b, c)
    print("The given triangle is:", triangle_type)
