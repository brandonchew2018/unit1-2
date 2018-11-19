#You will need to uncomment the problem calls at the bottom
import math
def problem1():
    print('What is your name?')
    name = input()
    print('Enter the width, height and length of the pool in that order.')
    w = float(input())
    h = float(input())
    l = float(input())
    rect = w * h * l * 7.5
    square = w * w * h * 7.5
    cyl = math.pi * (.5 * w) ** 2 * h * 7.5
    print('Hello ' + name)
    print('Your square pool will require ' + str(square) + ' gallons.' )
    print('Your rectangular pool will require ' + str(rect) + ' gallons.' )
    print('Your cylindrical pool will require ' + str(cyl) + ' gallons.' )
    
def problem2():
    print('Enter the four names.')
    name1 = input()
    name2 = input()
    name3 = input()
    name4 = input()
    print('Enter their GPAs.')
    grade1 = float(input())
    grade2 = float(input())
    grade3 = float(input())
    grade4 = float(input())
    print('The average GPAs of ' + name1 + ', ' + name2 + ', ' + name3 + ' and ' + name4 + ' is ' + str((grade1+grade2+grade3+grade4)/4) + '.')

def problem3():
    print('Enter a two digit number')
    num = int(input())
    print(str(num%10) + str(num//10))
    
def problem4():
    print('Enter a year')
    print((int(input()) // 100)+1)

def problem5():
    print('Enter the height the snails climbs, falls, and stops at, in that order.')
    c = float(input())
    f = float(input())
    g = float(input())
    h = 0
    p = True
    counter = 0
    while(p):
        counter += 1
        h += c
        if(h >= g):
            p = False
        h -= f
    print(counter)

def problem6():
    print('Enter your day number')
    print((int(input())-4)%7)


#This while loop has been provided to increase ease of case testing
while(True):
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    problem5()
    #problem6()
    

