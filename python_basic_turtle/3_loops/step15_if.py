from turtle import *

families = ['ウミガメ', 'リクガメ', 'カミツキガメ']

for i in range(3):
    if families[i] == 'ウミガメ':
        write(families[i])
        forward(100)

mainloop()