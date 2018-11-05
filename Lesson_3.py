def problem1():
    a = int(input())
    b = int(input())
    if(a > b):
        print(b)
    else:
        print(a)
        
def problem2():
    a = int(input())
    if(a < 0):
        print(-1)
    elif(a > 0):
        print(1)
    else:
        print(a)
        
def problem3():
    a = int(input())
    b = int(input())
    c = int(input())
    if(a < b and a < c):
        print(a)
    elif(b < a and b < c):
        print(b)
    else:
        print(c)
    
def problem4():
    a = int(input())
    b = int(input())
    c = int(input())
    if(a == b or b == c or a == c):
        if(a == b and b == c):
            print(3)
        else:
            print(2)
    else:
        print(0)

def problem5():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if((x1 == x2) != (y1 == y2)):
        print('YES')
    else:
        print('NO')
        
def problem6():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if(((x1-x2)+(y1-y2))%2 == 0):
        print('YES')
    else:
        print('NO')
        
def problem7():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if((abs(x1-x2) <= 1) and (abs(y1-y2) <= 1)):
        print('YES')
    else:
        print('NO')
        
def problem8():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if((x1+y1) == (x2+y2) or (x1-y1) == (x2-y2)):
        print('YES')
    else:
        print('NO')

def problem9():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if((x1+y1) == (x2+y2) or (x1-y1) == (x2-y2) or (x1 == x2) or (y1 == y2)):
        print('YES')
    else:
        print('NO')
        
def problem10():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if((abs(x1-x2) == 1 and abs(y1-y2) == 2) or (abs(x1-x2) == 2 and abs(y1-y2) == 1)):
        print('YES')
    else:
        print('NO')

def problem11():
    n = int(input())
    m = int(input())
    k = int(input())
    b = 'NO'
    for x in range(n):
        if(((n-x) * m) == k):
            b = 'YES'
    for x in range(m):
        if(((m-x) * n) == k):
            b = 'YES'
    print(b)
    
def problem12():
    y = int(input())
    if((y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))):
        print('LEAP')
    else:
        print('COMMON')
