# classes
# Customer -names,email,kra,dob,gender
# BankAccount -Customer,account number,account  type,balance
from mimetypes import init


class Customer:
    def __init__(self,names:str,email:str,kra:str,dob:str,gender:str):
        self.names=names
        self.email=email
        self.kra=kra
        self.dob=dob
        self.gender=gender

    def show_details(self):
        print(f"Name : {self.names} and KRA PIN :{self.kra}")

    def __str__(self) -> str:
        return f"{self.names} {self.gender}"

class Account:
    def __init__(self,owner:Customer,acc_no:str,acc_type:str,balance:float):
        self.owner=owner
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.balance=balance

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("----------------")

    def deposit(self,amount:float):
        self.balance += abs(amount)

    def withdraw(self,amount:float):
        if amount> self.balance:
            print("INSUFFICIENT BALANCE!")
        else:
            self.balance -= abs(amount)
    def __str__(self) -> str:
        return f"{self.acc_no} {self.owner}"

owner1=Customer("Jim Jong","jj123@gmail.com","KRA001","31-08-2005","MALE")
owner2=Customer("George Mbugua","mbugua123@gmail.com","KRA002","19-01-2007","MALE")
owner3=Customer("Alice Kings","alice123@gmail.com","KRA003","29-07-1998","FEMALE")

acc1=Account(owner1,"98765","current",80_000)
acc2=Account(owner2,"98766","savings",100_000)
acc3=Account(owner3,"98767","current",9_000_000)

acc1.print_details()
acc1.deposit(10000)
acc1.print_details()

print(acc1.owner)
print(acc3)