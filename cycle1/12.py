def count_vowels(string):

    vowel_counts = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}


    string = string.upper()


    for char in string:

        if char in vowel_counts:

            vowel_counts[char] += 1

    return vowel_counts

try:
    print("Register no:SJC22MCA-2014")
    print("Name       :Ashin Siby")
    print("Batch      :2022-2024")
    print("------------------------")
    input_string = input("Enter a string: ")


    vowel_counts = count_vowels(input_string)


    print("Vowel counts:")
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")
except ValueError:
    print("Invalid input. Please enter a valid string.")