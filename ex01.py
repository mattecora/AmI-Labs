try:
    n1 = int(input("Insert first number: "))
    n2 = int(input("Insert second number: "))
    print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(n1+n2))
except ValueError:
    print("Error! Not a number.")