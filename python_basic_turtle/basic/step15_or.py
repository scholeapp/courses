from turtle import *

user_input = input('かめ？ まる？: ')

if user_input == 'かめ' or user_input == 'カメ':
    shape('turtle')
elif user_input == 'まる':
    shape('circle')
else:
    shape('arrow')

mainloop()