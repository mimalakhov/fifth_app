#First
import re
def f_password(password):
    try:
        assert (len(password)>=6) and (len(re.findall("[0-9]", password)) != 0) and (not password.isdigit()) and (password.lower() != "password")
        print("Password is correct: {}".format(password))
    except AssertionError:
        print('Wrong!!!Try again!')
        print("Enter password:")
        f_password(input())

print("Enter password:")
f_password(input())
print()

#Second
def sum_arguments(list):
    print("Sum: {}".format(sum(list)))

arguments=[]
while True:
    try:
        print("Enter new argument? 0/1")
        answer=int(input())
        assert answer==1
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
        if (answer==0): break
        print("Wrong! Try again!")
        pass
print("Arguments: {}".format(arguments))
sum_arguments(arguments)
print()

#Third
def enter():
    while True:
        print("Enter an index:")
        try:
            index=int(input())
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
    if(index==1): return 1
    elif(index==2): return 1
    else: return fib(index-1) + fib(index-2)

print("Your number is: {}". format(fib(enter())))