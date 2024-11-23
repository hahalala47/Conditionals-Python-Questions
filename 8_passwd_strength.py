User_Password = input("Enter your password: ")
Password = len(User_Password)

if Password < 6:
        strength = "Weak"
elif Password <= 10:
        strength = "Medium"
else:
        strength = "Strong"

print("your password is", strength)