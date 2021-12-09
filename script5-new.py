#First_________________________________________________________________________________________
''' Написать функцию, принимающую строку-пароль. 
    Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. 
    Условия:
        ◦ Должен быть не менее 6 символов;
        ◦ Должен содержать хотя бы одну цифру;
        ◦ Не должен состоять только из цифр;
        ◦ Не должен содержать слово “password” в любом регистре.
'''

import re
def f_password(password):
    '''Функция принимает на вход пароль и возращает его, если всё ок
       или вызывается заново, если на вход поступил некорректный пароль'''
    try:
        assert (len(password) >= 6) and (len(re.findall("[0-9]", password)) != 0) and (not password.isdigit()) and (password.lower() != "password")
        print("Your password is: {}".format(password))
    except AssertionError:
        print('Wrong!!!Try again!')
        print("Enter password:")
        f_password(input()) # Рекурсия для повторного вызова функции, если пользователь ввёл некорректный пароль 

print("Enter password:")
f_password(input())
print()

#Second_________________________________________________________________________________________
''' Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.
'''

def sum_arguments(list):
    '''Функция принимает на вход список аргументов и возвращает их сумму'''
    print("Sum: {}".format(sum(list)))

arguments=[]

while True: # Стандартный цикл для пользовательского ввода (теперь с проверкой)
    try:
        print("Enter new argument? 0/1")
        answer = int(input())
        assert answer == 1
        print("Enter value: ")
        try:
            arguments.append(int(input()))
        except ValueError:
            print("Wrong! Try again!")
            pass
    except ValueError:
        print("Wrong! Try again!")
        pass
    except AssertionError:
        if (answer==0): 
            break
        print("Wrong! Try again!")
        pass
print("Arguments: {}".format(arguments))
sum_arguments(arguments)
print()

#Third________________________________________________________________________________
'''Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия)
'''
def enter():
    '''Ввод индекса, выделенный в функцию
       Индекс проходит проверку на положительность и вообще на корректность'''
    while True:
        print("Enter an index:")
        try:
            index = int(input())
            assert index > 0
            break
        except ValueError:
            print("This is not a nunber!")
            pass
        except AssertionError:
            print("Index must be a positive number!")
            pass
    return index

def fib(index):
    '''Стандартная функция для вывода n-ого числа Фибоначчи'''
    if(index==1): 
        return 1
    elif(index==2): 
        return 1
    else: 
        return fib(index-1) + fib(index-2)

print("Your number is: {}". format(fib(enter())))