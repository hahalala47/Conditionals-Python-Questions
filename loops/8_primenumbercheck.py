User_Input = int(input("Please enter any number you want to check , it's prime or not: \n"))

isit_prime = True 
if User_Input > 1:
    for Unknown_number in range(2, User_Input):
        if User_Input % Unknown_number == 0:
            isit_prime = False
            break
print(isit_prime)
