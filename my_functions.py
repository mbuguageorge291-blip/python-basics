import math


def greet():
    print("hello world")
greet()

def greeting(user):
    print(f"hello {user}, welcome to Python")
greeting("George")

def area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return area