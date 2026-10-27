# creating a list
people=["Jack","Jane","Juma","Job"]
scores=[51,62,83,74,55,46,37,28,89,70]
print(people[0])
print(scores[0])

# adding  to a list using append
people.append("George")
print(people)

# sort a list of the scores
scores.sort()
print(scores)
print(scores[0],scores[-1])

#beginning from the highest to the lowest
scores.sort(reverse=True)
print(scores)

# adding the numbers
print(sum(scores))

# finding mean
total=len(scores)
print(sum(scores)/total)

# slicing (to cut a bit)
scores.sort(reverse=True)
print(scores[-2:])
print(scores[:2])
print(scores[3:5])

# CREATING A SET-used to remove duplicates
numbers={87,90,87,67,78,67,54}
print(numbers)

# tuple -used to store immutable data(once created no one can alter it)
days=("Monday","Tuesday","Wednesday","Thursday","Friday")
print(days)

# dictionary -used to contain key + value
person={"Name" : "James", "Age" :25}
print(person["Name"])
print(person["Age"])

# data structures and algorithm
print(sum(numbers))
watu=[{"Name" : "George", "Age" :25},{"Name" : "Samson", "Age" :25},{"Name" : "Julia", "Age" :25}]
print(watu[2]["Name"])