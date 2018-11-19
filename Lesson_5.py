import math
def problem1():
    s = str(input())
    print( s[2])
    print( s[-2])
    print(s[:5])
    print(s[:-2])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))
    
def problem2():
    print(int(str(input()).count(' ')+1))

def problem3():
    s = str(input())
    print(s[int(math.ceil(len(s)/2)):] + s[:int(math.ceil(len(s)/2))])
    
def problem4():
    n = str(input())
    print(n[n.find(' ')+1:] , n[:n.find(' ')+1])

def problem5():
    s = str(input())
    if(s.find('f') != -1):
        if(s.find('f') != s.rfind('f')):
            print(s.find('f'), s.rfind('f'))
        else:
            print(s.find('f'))
            
def problem6():
    s = str(input())
    if(s.find('f') == -1):
        print (-2)
    else:
        if((s.find('f', s.find('f') + 1)) == -1):
            print (-1)
        else:
            print(s.find('f', s.find('f') + 1))
            
def problem7():
    s = str(input())
    print(s[:s.find('h')] + s[s.rfind('h')+1:])
    
def problem8():
    s = str(input())
    print(s[:s.find('h')] + s[s.rfind('h') : s.find('h')-1 : -1] + s[s.rfind('h')+1:])
    if(s[0] == 'h' and s[len(s)-1] == 'h'):
        print(s[::-1])

def problem9():
    print(str(input()).replace('1', 'one'))

def problem10():
    print(str(input()).replace('@', ''))

def problem11():
    s = str(input())
    print(s[:s.find('h') +1] + s[s.find('h')+1 : s.rfind('h')].replace('h', 'H') + s[s.rfind('h'):])

def problem12():
    s = str(input())
    for x in range(len(s)):
        if(x % 3 != 0):
            print(s[x], end='')

problem12()