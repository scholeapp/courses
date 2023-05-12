from turtle import *

s = int(input('スピードは？ (1 - 10)'))

if  7 <= s <= 10:
    write('はやい')
elif 3 <= s < 7:
    write('ふつう')
else:
    write('おそい')

speed(s)
forward(100)

mainloop()