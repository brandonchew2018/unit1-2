def problem1():
    i = 1
    n = int(input())
    while(i ** 2 <= n):
        print(int(i ** 2) ,end = ' ')
        i += 1

def problem2():
    n = int(input())
    i = 2
    while(n%i != 0):
        i+=1
    print(i)
    
def problem3():
    n = int(input())
    i = 0
    while(2 ** (i+1) <= n):
        i+=1
    print(i, 2 ** i)
    
def problem4():
    x, y = float(input()), int(input())
    i = 1
    while(x < y):
        x *= 1.1
        i += 1
    print(i)
    
def problem5():
    i = 0
    while(int(input()) != 0):
        i+=1
    else:
        print(i)
        
def problem6():
    i = 0
    while(True):
        n = int(input())
        if(n == 0):
            break
        i += n
    print(i)

def problem7():
    sum = 0
    i = 0
    while(n != 0):
        sum += n
        i += 1
        n = int(input())
    print(sum/float(i))

def problem8():
    n = int(input())
    s = 0
    while(n != 0):
        if(n > s):
            s = n
    n = int(input())
    print(s)
    
def problem9():
    n = int(input())
    i = 1
    m = 0
    while(n != 0):
        if(m < n):
            m = n
            ind = i
        i += 1
    n = int(input())
print(ind)
    
def problem10():
    n = int(input())
    i = 0
    while(n != 0):
        if(n % 2 == 0):
            i += 1
        n = int(input())
    print(i)

def problem11():
    n = int(input())
    f = n
    i = 0
    while(n != 0):
        if(n > f):
            i += 1
        f = n
        n = int(input())
    print(i)
    
def problem12():
    n = int(input())
    f = n
    i = 0
    while(n != 0):
        if(n > f):
            i += 1
        f = n
        n = int(input())
    print(i)

def problem13():
    n = int(input())
    m = 0
    i = 1
    while(n != 0):
        if(n > m):
            m = n
            i = 1
        elif(n == m):
            i += 1
        n = int(input())
    print(i)

def problem14():
    f = 1
    s = 0
    for x in range(int(input())):
        f, s = f + s, f
    print(s)
    
def problem15():
    f = 1
    s = 0
    i = 0
    n = int(input())
    while(True):
        if(s == n):
            print(i)
            break
        elif(s > n):
            print(-1)
            break
        f, s = f + s, f
        i += 1
    
def problem16():
    n = int(input())
    prev = 0
    length = 1
    maxLength = 1
    while(n != 0):
        if(n == prev):
            length += 1
            maxLength = max([maxLength, length])
        else:
            length = 1
        prev = n
        n = int(input())
    print(maxLength)

problem1()