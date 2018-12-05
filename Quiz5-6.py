def problem1():
    s = str(input())
    if(len(s) < 2):
        print('')
    else:
        print(str(s[:2] + s[-2:]))

def problem2():
    s = str(input())
    res = s[0]
    for x in range(1,len(s)):
        if(s[x] == s[0]):
            res += '$'
        else:
            res += s[x]
    print(res)

def problem3():
    s = str(input())
    res = ''
    for x in range(0, len(s), 2):
        res += s[x]
    print(res)
        
def problem4():
    user_input = 0
    while(user_input != 8):
        print('Guess a number between 0 and 9 inclusive!')
        user_input = int(input())
    print('Well guessed!')

def problem5():
    s = str(input())
    c = 0
    for x in range(len(s)):
        if(int(s[x])%2 == 0):
            c += 1
    print("There are " + str(c) + " even numbers and " + str(int(len(s)-c)) + " odd numbers")

def problem6():
    x = float(input())
    while(x > 0):
        print(x)
        x -= .5


def problem7():
    for x in range(1, 27, 2):
        print((x ** .5))


problem6()
    