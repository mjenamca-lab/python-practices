#String declarion
my_Name= "Melina"
print(my_Name)
print(len(my_Name))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))

#Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.               
That is why I created 30 days of python.'''
print(multiline_string) 
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.   
That is why I created 30 days of python."""
print(multiline_string)
# String Concatenation
first_name = "Melina"
last_name = "Mohapatra"
space = " "
full_name = first_name + space + last_name
print(full_name) # Melina Mohapatra

#unpacking characters
language = "Python"
a,b,c,d,e,f = language # unpacking sequence characters into variables   
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
# Accessing characters in strings by index
language = "Python"
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

