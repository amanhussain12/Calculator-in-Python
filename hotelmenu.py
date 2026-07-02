# menu = {
#     "pizza":750,
#     "zinger burger":400,
#     "roll":200,
#     "broast":450,
#     "chicken tikka":480,
#     "paratha":80,
#     "cold drink":120,
#     "salad":70,
#     "club sanwich":420,
# }

# print("Welcome to Hussain Restaurant")
# print("Pizza : Rs:750\nzinger burger : Rs:400\nRoll : Rs:200\nbroast : Rs:450\nchicken tikka : Rs:480\nparatha : Rs:80\ncold drink : Rs:120\nsalad : Rs:70\nclub sanwich : Rs:420")

# order_total = 0

# item_1 = input("Enter the name of item you want to order = ")

# if item_1 in menu:
#     order_total += menu[item_1]
#     print(f"your item {item_1} has been added your order") 

# else:
#     print(f"{item_1} is not available yet!")

# another_order = input("Do you want to another order? (yes/no) = ")

# if another_order == "yes":
#     item_2 = input("Enter the name of second item = ")

#     if item_2 in menu:
#         order_total += menu[item_2]
#         print(f"your item {item_2} has been added your order")

#     else:
#         print(f"{item_2} is not available yet!")

# print(f"the total amount of items to pay is {order_total}")

menu = {
    "pizza":750,
    "zinger burger":400,
    "roll":200,
    "broast":450,
    "chicken tikka":480,
    "paratha":80,
    "cold drink":120,
    "salad":70,
    "club sanwich":420,
}

print("Welcome to Hussain Restaurant")
print("Pizza : Rs:750\nzinger burger : Rs:400\nRoll : Rs:200\nbroast : Rs:450\nchicken tikka : Rs:480\nparatha : Rs:80\ncold drink : Rs:120\nsalad : Rs:70\nclub sanwich : Rs:420")

order_total = 0

while True:
    item_1 = input("Enter the name of item you want to order = ").lower()

    if item_1 in menu:
        order_total += menu[item_1]
        print(f"your item {item_1} has been added your order")
    
    else:
        print(f"{item_1} is not available yet!")
    
    another_order = input("Do you want to another order? (yes/no) = ").lower()

    if another_order == "yes":
        continue
    
    if another_order == "no":
        break

print(f"the total amount of items to pay is {order_total}")
