from turtle import *

user_input = input('かめ？ まる？: ')

if user_input == 'かめ':
    shape('turtle')
elif user_input == 'まる':
    shape('circle')
else:
    shape('arrow')

mainloop()