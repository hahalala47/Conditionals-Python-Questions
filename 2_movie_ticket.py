age = input("!Please, Enter your age: \n")
int_age = int(age)
day = "Wednesday"

price = 12 if int_age>=18 else 8

if day == "Wednesday":
        Ticket_Price = price - 2
        print("the price of the Ticket is $",Ticket_Price)