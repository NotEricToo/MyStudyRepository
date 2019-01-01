from tkinter import *
import random
import tkinter.simpledialog as dl 
import tkinter.messagebox as mb 

# mb.showinfo('Hello Man','Welcome to Guess Number Game!')

# guess = dl.askinteger('Guess Number', 'Please input a number between 1-100')

# print(guess)

root= Tk()
w=Label(root,text="Welcome to Guess Number Game!")
w.pack()

def game(): 
    number = random.randint(1,100)
#     print(number)
      
    def game_f():
        global j
#         i = int(input('Please input a number : '))
        i = dl.askinteger("GuessNumber", "Enter a number [1-100]")
#         print('Your input number is : ' + str(i))
#         mb.showinfo('MeesageBOx','Your input number is {}'.format(i))
        j = j + 1     
        print('You guess {0} times now , the number you guess is {1}'.format(j,i)) 
        if number == i  : 
#             print('You guess right, the number is ' + str(number))
            mb.showinfo('MeesageBOx','You guess right, the number is {}'.format(number))
            return True
        elif number > i :
#             print('LOW !! '*3 + str(i))
            mb.showinfo('MeesageBOx','{} is too LOW !!! '.format(i))
            return False
        else: 
#             print('HIGH !! '*3 + str(i))
            mb.showinfo('MeesageBOx','{} is too High !!! '.format(i))
            return False
         
         
      
    while True:
      if game_f() :
#           print('Game end la, and you guess {0} times then get the result '.format(j))
        mb.showinfo('MeesageBOx','Game end la, and you guess {0} times then get the result '.format(j))
        break
       
 
j = 0 
game()



