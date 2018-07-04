my_str = input("Insert a string: ")
my_len = len(my_str)
if my_len < 4:
    print("String too short!")
else:
    print(my_str[0] + my_str[1] + my_str[my_len-2] + my_str[my_len-1])