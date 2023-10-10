import numpy as np
print("Register no:SJC22MCA-2014")
print("Name       :Ashin Siby")
print("Batch      :2022-2024")
print("------------------------")
# Create a 2x3 array with complex data type elements
complex_array = np.array([[1 + 2j, 3 + 4j, 5 + 6j],
                          [7 + 8j, 9 + 10j, 11 + 12j]])

# Print the complex array
print(complex_array)

num_rows, num_columns = complex_array.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

dimensions = complex_array.shape
print(f"Dimensions of the array: {dimensions}")

reshaped_array = complex_array.reshape(3, 2)
print("Reshaped 3x2 Array:")
print(reshaped_array)
