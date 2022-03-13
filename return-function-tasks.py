# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:54:07 2022

@author: sherz
"""
def find_prime_num(min,max):
    '''The function that counts prime numbers'''
    prime_numbers = []    
    for n in range(min, max+1):
        prime = True
        if n == 1:
            prime = False
        elif n == 2:
            prime = True
        else:
            for x in range (2,n):
                if (n%x == 0):
                    prime = False
        if prime:
            prime_numbers.append(n)
    return prime_numbers
find_prime_num(1,35)
            
    
def find_fibonacci(n):
    '''The function that counts Fibonacci's numbers'''
    fib_numbers = []
    for x in range(n):
        if x==0 or x==1:
            fib_numbers.append(1)
        else:
            fib_numbers.append(fib_numbers[x-1] + fib_numbers[x-2])
    return fib_numbers
print(find_fibonacci(21))


def find_bigger(x, y, z):
    bigger = max(x,y,z)
    return bigger
z=float(input("1st number >>>"))
x=float(input("2nd number >>>"))
y=float(input("3rd-number >>>"))
print(find_bigger(x, y, z))


def circle_info(radius, pi=3.1417):
    circle = {"radius":radius,
              "diameter":2*pi,
              "perimeter":2*pi*radius,
              "area":pi*radius**2}
    return circle
circle_info(4)


def client_info(firstname, surname, byear, bplace, email='', tel=None):
    '''return informations about client as a function'''
    client = {'name':firstname,
              'surname':surname,
              'birthyear':byear,
              'birthplace':bplace,
              'age':2022-byear,
              'email':email,
              'phone':tel}
    return client

print('We will create list of clients.')
clients = []
while True:
    name = input("Enter firstname: ")
    sname = input("Enter surname: ")
    by = int(input("Enter year of birth: "))
    bp = input("Enter place of birth: ")
    email = input("Enter email: ")
    number = input("Enter phone number: ")
    
    clients.append(client_info(name, sname, by, bp, email, number))
    answer = input("Do you want to add any clients (yes/no)\n")
    if answer == "no":
        break
#    elif answer.lower() != "yes":
#        print()
print('Clients: ')
for client in clients:
    print(f"{client['name'].title()} {client['surname'].title()},"
          f" {client['age']} years old. Phone: {client['phone']}."
          f" Email: {client['email']} and was born in {client['birthplace'].title()}")      
    

