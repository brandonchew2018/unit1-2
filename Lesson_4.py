def problem1():
    a = int(input())
    b = int(input())
    for x in range(a, b+1):
        print(x)
        
def problem2():
    a = int(input())
    b = int(input())
    if(a < b):
        for x in range(a, b+1):
            print(x)
    else:
        for x in range(a, b-1, -1):
            print(x)
            
def problem3():
    n = 0;
    for x in range(10):
        n += float(input())
    print(n)
    
def problem4():
    n = int(input())
    a = 0
    for x in range(n):
        a += float(input())
    print(a)

def problem5():
    a = 0
    for x in range(1,int(input()+1)):
        a += x ** 3
    print(a)
    
def problem6():
    n = 1
    for x in range(1,  int(input())+1):
        n *= x
    print(n)
    
def problem7():
    n = 0
    for x in range(int(input())):
        if(int(input()) == 0):
            n += 1
    print(n)

def problem8():
    n = 0
    m = 1
    for x in range (1,int(input())+1):
        m *= x
        n += m
    print(n)
    
def problem9():
    n = int(input())
    for x in range (1,n+1):
        string = ''
        for y in range (1, x+1):
            string += str(y)
        print(string)
        
def problem10():
    n = int(input())
    res = 0
    for x in range(n+1):
        res += x
    for x in range(n-1):
        res -= int(input())
    print(res)