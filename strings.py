name='George'
sentence='My home area is called \"Limuru\"'
print(name)
print(sentence)

# operations inbuilt in python to work on strings

# to print in capital letters
print(name.upper())
print(sentence.upper())

# to print in small letters
print(name.lower())
print(sentence.lower())

sentence=sentence.lower()
print(sentence)

#counting how many times a letter is occuring
print(sentence.count('h'))

# to replace
sentence.replace('h','j')
sentence=sentence.replace('h','j')
print(sentence)
print(sentence.count('j'))

result=name.isnumeric()
print(result)
