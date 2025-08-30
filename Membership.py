
age = int(input("Enter your age: "))
membership = input("Are you a member? (yes/no): ").strip().lower()
if age >= 18 and membership == "yes":
    print("Full access granted")
elif age < 18 and membership == "yes":
    print("Sorry, you must be at least 18 years old to get full access.")
elif age >= 18 and membership == "no":
    print("Sorry, you must be a member to get full access.")
else:
    print("Sorry, you must be at least 18 and a member to get full access.")
