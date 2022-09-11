'''
Question 1: Design Magic 8 Ball Program In Python 
'''
import random

#  print(dir(random))  ;to check all the methods available in random

''' 
  These are some of random functions:
  
 'choice', 'choices', 
 'randint', 'random', 'randrange', 'sample', 'seed', 
 'setstate', 'shuffle', 'triangular', 'uniform' 

'''
def magic8ball():
    response=input("(Press 'any key' for answer and 'quit' to exit )\n What is your question?")
    EightBall_answers=[
         "I didn't get that can you repeat",
         "Outlook good",
         "You may rely on it",
         "Ask again later",
         "Concentrate and try again",
         "Reply hazy,try again",
         "My reply is no",
         "My sources say no"
        ]   
    if response=='quit':
        print("Have a nice day!!!")
    else:
        print(random.choice(EightBall_answers))
        magic8ball()
magic8ball()
