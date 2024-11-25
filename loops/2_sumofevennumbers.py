number = input("Enter any number")
numbers = int(number)
sumof_even_number = 0

for value in range(1, numbers + 1):
    if value % 2 == 0:
        sumof_even_number += 1
print("the sum of the even number is :", sumof_even_number)

