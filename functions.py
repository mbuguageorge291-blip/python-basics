# functions
import random

with open("data.txt","w") as file:
    # file.write("Age\n")
    # file.write("Name\n")
    for temp in range(100):
        x=random.randint(1,100)
        file.write(str(x)+"\n")

