phone_book = {
    "Shreya": "9876543210",
    "Aman": "9871234567",
    "Priya": "9874561230"
}

name = input("Enter name: ")

if name in phone_book:
    print("Phone Number:", phone_book[name])
else:
    print("Contact not found")