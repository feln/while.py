import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return'its certain'
    elif answerNumber==2:
        return'its decidedly so'
    elif answerNumber==3:
        return'yes'
    elif answerNumber==4:
        return'replay hazy try again'
    elif answerNumber==5:
        return'ask again later'
    elif answerNumber==6:
        return'concentrate and ask again'
    elif answerNumber==7:
        return'my replay is no'
    elif answerNumber==8:
        return'outlook not so good'
    elif answerNumber==9:
        return'very doubtful'
r=random.randint(1,9)
fortune=getAnswer(r)
print(fortune)