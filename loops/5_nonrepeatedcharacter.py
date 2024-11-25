input_str = "llauda"

for non_repeat in input_str: 
    print(non_repeat)
    if input_str.count(non_repeat) == 1:
        print("the first non repeat character is: ",non_repeat)
        break
