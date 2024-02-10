
from tkinter import *
from tkinter import messagebox
import random


frame = Tk()
color = '#212F3D'
fg='white'

frame.config(bg=color)
frame.geometry('1079x754+457+122')

# edit text
head = Label(frame,text='Enter players') ; head.config(font=("impact",30),bg=color,fg=fg)\
        ; head.pack(side=TOP,pady=5)


# input element -> Text area
Text_area = Text(frame,width=25,height=8);Text_area.config(font=('Normal',20));Text_area.pack()


# output
f = Label(frame, text='First group') ; f.config(font=("impact",25), bg=color, fg=fg,\
    padx=10);f.pack(side=LEFT)

s = Label(frame, text='Second group') ;s.config(font=("impact",25),bg=color,\
    fg=fg, padx=10);s.pack(side=RIGHT)

f_list = Listbox(frame,width=20,height=8) ;f_list.config(font=('impact',20)) ;f_list.pack(side=LEFT)
s_list = Listbox(frame,width=20,height=8) ;s_list.config(font=('impact',20)) ;s_list.pack(side=RIGHT)

def onclick():
    print(frame.geometry())
    f_list.delete(0, END)
    s_list.delete(0, END)
    players_name = Text_area.get('1.0', END)
    player_group = []
    player_list = players_name.split('\n')
    player_list = list(player_list)
    player_list.remove("")
    for i in range(0, len(player_list), 1):
        rand = random.randint(0, (len(player_list) - 1))
        player = player_list[rand]
        if player not in player_group:
            player_group.append(player)
        else:
            while player in player_group:
                rand = random.randint(0, (len(player_list) - 1))
                player = player_list[rand]
                if player not in player_group:
                    player_group.append(player)
                    break

    first_group = player_group[:int((len(player_group) / 2))]
    second_group = player_group[int((len(player_group) / 2)):]

    for i in range(0, len(first_group), 1):
        f_list.insert(END, f'{i + 1}- {first_group[i]}')

    for j in range(0, len(second_group), 1):
        s_list.insert(END, f'{j + 1}- {second_group[j]}')



b = Button(frame,text='click',width=10) ; b.config(font=('impact',17),command= onclick) ; \
    b.pack(side=BOTTOM,pady=5,padx=5)

frame.mainloop()











