from tkinter import *
import random

answers=["apple","mango","banana",'achieve','kolkata','evening','servant','receiver',
         'london','ferrari','hollow','horror','master','morning','bottle','pen','router',
         'copy','narrow','wide','dive','love','block','right','simple','deaf','single',
         'knight','hope', 'accept', 'caught', 'arrive','course', 'beyond', 'budget',
         'during', 'device','bishop', 'burden','easily','differ']

anagram_list = []
for i in answers:
    anagram_list.append("".join(random.sample(i,len(i))))
print(anagram_list)
win = Tk()
win.title("Text To Speech")
title = Label(win,text="Anagram solver game",font=40)
display_word = Label(win,text="",font=50)
answer_box = Entry(win,font=20)
submit_but = Button(win,text="Submit Answer")
reset_but = Button(win,text="Reset")
running_total = Label(win,text="")

title.pack()
display_word.pack()
answer_box.pack()
submit_but.pack()
reset_but.pack()
running_total.pack()

win.mainloop()