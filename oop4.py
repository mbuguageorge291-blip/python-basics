# inheritance

# employees -name,ID ,department,gender
# salaried --salary,contract
# casual --rates

class Employee:
    def __init__(self,names:str,id_number:str,department:str,gender:str):
        self.names=names
        self.id=id_number
        self.dept=department
        self.gender=gender

    def print_details(self):
        print(self.names)
        print(self.id)
        print(self.dept)
        print(self.gender)
        print("------------")

    def print_names(self):
        print(f"Name is {self.names}")

class SalariedEmployee(Employee):
    def __init__(self, names: str, id_number: str, department: str, gender: str,salary:int,tenure:int):
        super().__init__(names, id_number, department, gender)
        self.tenure=tenure
        self.salary=salary

class CasualWorker(Employee):
    def __init__(self, names: str, id_number: str, department: str, gender: str,rate:float):
        super().__init__(names, id_number, department, gender)
        self.rate=rate
    def calc_wage(self,hours:float):
        return hours * self.rate


s1=SalariedEmployee("GEORGE MBUGUA","001","HR","MALE",100_000,5)
c1=CasualWorker("AHMED JUMA","101","CATERING","MALE",356)

s1.print_details()
c1.print_details()
print(c1.calc_wage(19))

c1.print_names()

