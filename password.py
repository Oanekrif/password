import random
length = input("enter length of password: ")
password = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_char = '1234567890-!@#$%^&*()_+?[]"|<>'
for i in range(int(length)):
    random_char = random.choice(lowercase + uppercase + special_char)
    password = password + random_char
print("password dyalek howa: "+password)