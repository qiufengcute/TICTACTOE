import random

x = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
if random.randint(0,1) == 0:
    y = 'x'
else:
    y = 'o'

def run():
    global x,y
    if y == 'x':
        while True:
            a = str(input('请x输入下的位置：'))
            if a.isdigit():
                a = int(a)
                if a > 0 and a < 10 and x[a - 1] == ' ':
                    x[a - 1] = 'X'
                    print('好的')
                    break
                else:
                    print('不行！')
            else:
                print('不行！')
        y = 'o'
    else:
        while True:
            a = str(input('请o输入下的位置：'))
            if a.isdigit():
                a = int(a)
                if a > 0 and a < 10 and x[a - 1] == ' ':
                    x[a - 1] = 'O'
                    print('好的')
                    break
                else:
                    print('不行！')
            else:
                print('不行！')
        y = 'x'

def look():
    global x
    ii = 'X'
    p = 0
    if x[p] == ii and x[p+1] == ii and x[p+2] == ii:
        input('x赢了')
        exit()
    elif x[p+3] == ii and x[p+4] == ii and x[p+5] == ii:
        input('x赢了')
        exit()
    elif x[p+6] == ii and x[p+7] == ii and x[p+8] == ii:
        input('x赢了')
        exit()
    elif x[p] == ii and x[p+3] == ii and x[p+6] == ii:
        input('x赢了')
        exit()
    elif x[p+1] == ii and x[p+4] == ii and x[p+7] == ii:
        input('x赢了')
        exit()
    elif x[p+2] == ii and x[p+5] == ii and x[p+8] == ii:
        input('x赢了')
        exit()
    elif x[p] == ii and x[p+4] == ii and x[p+8] == ii:
        input('x赢了')
        exit()
    elif x[p+2] == ii and x[p+4] and x[p+6] == ii:
        input('x赢了')
        exit()
    ii = 'O'
    if x[p] == ii and x[p+1] == ii and x[p+2] == ii:
        input('o赢了')
        exit()
    elif x[p+3] == ii and x[p+4] == ii and x[p+5] == ii:
        input('o赢了')
        exit()
    elif x[p+6] == ii and x[p+7] == ii and x[p+8] == ii:
        input('o赢了')
        exit()
    elif x[p] == ii and x[p+3] == ii and x[p+6] == ii:
        input('o赢了')
        exit()
    elif x[p+1] == ii and x[p+4] == ii and x[p+7] == ii:
        input('o赢了')
        exit()
    elif x[p+2] == ii and x[p+5] == ii and x[p+8] == ii:
        input('o赢了')
        exit()
    elif x[p] == ii and x[p+4] == ii and x[p+8] == ii:
        input('o赢了')
        exit()
    elif x[p+2] == ii and x[p+4] and x[p+6] == ii:
        input('o赢了')
        exit()
    elif ' ' not in x:
        input('平局')
        exit()

while True:
    print(x[0],'|',x[1],'|',x[2],sep='')
    print('—————')
    print(x[3],'|',x[4],'|',x[5],sep='')
    print('—————')
    print(x[6],'|',x[7],'|',x[8],sep='')
    run()
    look()
