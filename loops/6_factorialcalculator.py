number_for_factorial = 5
number_tostart_factorial = 1

while number_for_factorial > 0:
    number_tostart_factorial *= number_for_factorial
    number_for_factorial -= 1
print(number_tostart_factorial)