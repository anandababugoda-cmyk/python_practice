name = input("Enter student name: ")

m1 = int(input("Enter English marks: "))
m2 = int(input("Enter Maths marks: "))
m3 = int(input("Enter Science marks: "))

total = m1 + m2 + m3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)