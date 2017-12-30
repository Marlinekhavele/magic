import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
            return 'It is so'
    elif answerNumber ==3:
                return 'yes'
    elif answerNumber ==4:
        return 'try again'
    elif answerNumber ==5:
        return 'Ask again later'
    elif answerNumber ==6:
        return 'reply'
    elif answerNumber ==7:
        return 'ask again'
    elif answerNumber == 8:
        return 'not good'
    elif answerNumber ==9:
        return 'doubtful'
        
        
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
