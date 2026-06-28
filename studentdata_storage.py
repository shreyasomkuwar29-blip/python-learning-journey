name = input("Enter Student Name: ")
age = input("Enter Age: ")
branch = input("Enter Branch: ")

file = open("students.txt", "a")

file.write(f"Name: {name}\n")
file.write(f"Age: {age}\n")
file.write(f"Branch: {branch}\n")
file.write("----------------------\n")

file.close()

print("Student information saved successfully!")