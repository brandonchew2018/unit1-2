def problem1():
    print('Please input an integer.')
    if(int(input())%10 == 7):
        print('YES')
    else:
        print('NO')
        
def problem2():
    print('Please input 3 different integers.')
    a = int(input())
    b = int(input())
    c = int(input())
    bool = 'YES'
    if(a > b):
        bool = 'NO'
        temp = a
        a = b
        b = temp
    if(b > c):
        bool = 'NO'
        temp = c
        c = b
        b = temp
    if(a > b):
        bool = 'NO'
        temp = a
        a = b
        b = temp
    print(bool)
    if(bool == 'NO'):
        print a,b,c
        
def problem3():
    print('Please input a 4 digit integer')
    s = str(input())
    if(s[0] == s[3] and s[1] == s[2]):
        print('YES')
    else:
        print('NO')
        

def problem4():
    print('Please input 3 vertices on a 2-dimensional plane in the format: "(x, y)"')
    c1 = str(input())
    c2 = str(input())
    c3 = str(input())
    if(c1[1] == c2[1]):
        x = c3[1]
    elif(c1[1] == c3[1]):
        x = c2[1]
    else:
        x = c1[1]
    if(c1[4] == c2[4]):
        y = c3[4]
    elif(c1[4] == c3[4]):
        y = c2[4]
    else:
        y = c1[4]
    print(int(x), int(y))
    
def problem5():
    print('Enter the inclusive upper bound of a list of numbers incrementing from 1.')
    for x in range (1, (int(input()) + 1)):
        print x
    
def problem6():
    print('Enter the inclusive bounds of bases of squares.')
    for x in range (int(input()), int(input()) + 1):
        print x**2
    
def problem7():
    print('Enter the exclusive bounds for prime search.')
    for x in range (int(input())+1, int(input())):
        valid = True
        for y in range (2, x):
            if(x % y == 0):
                valid = False
        if(valid or x == 1):
            print(x)

    
while(True):
    problem7()
