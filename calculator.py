print("1 plus")
print("2 minnas")
print("3 multiply")
print("4 divide")

option = int(input("Choose an operation Number : "))
result = 0

if(option in [1, 2, 3, 4]):
    num1 = int(input("Enter first Number : "))
    num2 = int(input("Enter Second Number : "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2
else:
    print("Invaild operation")

print("the result of the operation is {}". format(result))


