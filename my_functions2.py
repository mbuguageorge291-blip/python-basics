# def happy_birthday():
#     print("Happy birthday to you")
#     print("You are old")
#
# happy_birthday()


# def display_invoice(username,amount,due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:2f} is due: {due_date}")
#
# display_invoice("George",42.50,"01/01")

# def add(x,y):
#     z=x+y
#     return z
# def sub(x,y):
#     z=y-x
#     return z
# def multiply(x,y):
#     z=x*y
#     return z
#
# print(add(1,2))
# print(multiply(1,2))
# print(sub(1,2))
#

def create_name(first,last):
    first=first.upper()
    last=last.capitalize()
    return first +" "+ last

full_name=create_name("George","Mbugua")

print(full_name)

