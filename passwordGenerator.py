import random 

# creates password, 10 characters long.
print('your password: ')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?@#$%^*&!()?'


password = ''

for x in range(16):
    password += random.choice(chars)

print(password)
