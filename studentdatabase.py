student = {}
student ["name"] = input("Enter Name:")
student["roll_no"] = int(input("Enter Roll Number:"))
student["branch"] = input("Enter branch:")
student["cgpa"] = float(input("Enter CGPA:"))
print("\n Student Details")
for key , value in student.items():
    print(key, ":" , value)