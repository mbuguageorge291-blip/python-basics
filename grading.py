score=input("Enter your score:")
score=int(score)
# if statement
if score>=90:
    print("A")
elif 80 <= score < 90:
    print("A-")
elif 70 <= score < 80:
    print("B+")
elif 60 <= score < 70:
    print("B")
elif 40 <= score < 60:
    print("B-")
elif 30 <= score < 40:
    print("C")