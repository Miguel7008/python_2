import random
question = input()
answer_ran = random.randint(1,9)

if answer_ran == 1:
    answer_2 ='Yes- Definetly.'
elif answer_ran == 2:
    answer_2 = 'It is decidedly so.'
elif answer_ran == 3:
    answer_2 = 'Without a doubt.'
elif answer_ran == 4:
    answer_2 ='Relpy hazy, try again.'
elif answer_ran == 5:
    answer_2 ='Ask again later.'
elif answer_ran == 6:
    answer_2 ='Better not tell you now.'
elif answer_ran == 7:
    answer_2 ='My sources say no.'
elif answer_ran== 8:
    answer_2 ='Outlook not so good.'
elif answer_ran == 9:
    answer_2 = 'Very doubtful.'
else:
    answer_2 ='Error'

print('Question:    ' , question)
print('Magic 8 ball:      ' , answer_2)

'''
import random


question = input()

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Question:      ' + question) 
print('Magic 8 Ball:  ' + answer)
'''