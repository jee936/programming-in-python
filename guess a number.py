import random
n = random.choice(range(10))
for i in range(5):
    c = int (input('guess a number:'))
    if c==n:
        print('win')
        exit(0)
    else:
        print('try again')
        print('lost')



'''
sample ouytput:
 guess a number:8
 try again
 lost
 guess a number:7
 try again
 lost
 guess a number:6
 try again
 lost
 guess a number:5
 try again
 lost
 guess a number:4
 try again
 lost
 guess a number:3
 win
 '''
 
