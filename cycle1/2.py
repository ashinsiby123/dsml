n=int(input("Enter number of terms in series : "))
print("Register no:SJC22MCA-2014")
print("Name       :Ashin Siby")
print("Batch      :2022-2024")
print("------------------------")
n1=0
n2=1
count=0

if n<0:
    print("Please enter a positive number: ")
elif n==1:
    print("Fibonacci sequence upto ",n,":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
