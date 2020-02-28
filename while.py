import random
x=random.randint(1,37)
print(x)
trycount=0
while trycount < 5:
    tk = int(input('Guess:'))
    if tk == x:
        print('Bingo')
        break
    elif tk < x:
        print('toosmall')
        trycount += 1
    else:
        print('toobig')
        trycount += 1
else:
    print('over')