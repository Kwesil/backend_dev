import django

print('Create new account')

username = input("Enter a username:  ")
password = input("Enter your Password:  ")

print('Your account has been created succesfully.')
print('Login now!')

username1 = input('Enter your username:  ')
password1 = input('Enter your password:  ')

if username == username1 and password == password1:
    print('User loggged in successfully')
    
else:
    print('Invalid credentials')