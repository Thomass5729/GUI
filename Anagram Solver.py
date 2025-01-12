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

score = 0
attempts = 0
def submit_ans():
    global score,attempts,random_index
    attempts+=1
    answer = answer_box.get()
    if answer == answers[random_index]:
        score+=1
    running_total.config(text=f"Score: {score}/{attempts}")
    random_index = random.randint(0,len(answers))-1
    display_word.config(text=anagram_list[random_index])
    answer_box.delete(0,END)

def reset():
    global score,attempts,random_index
    attempts=0
    score=0
    running_total.config(text=f"Score: {score}/{attempts}")
    answer_box.delete(0,END)
    random_index = random.randint(0,len(answers))
    display_word.config(text=anagram_list[random_index])


win = Tk()
win.title("Anagram solver")
title = Label(win,text="Anagram solver game",font=40)
display_word = Label(win,text="",font=50)
answer_box = Entry(win,font=20)
submit_but = Button(win,text="Submit Answer",command=submit_ans)
reset_but = Button(win,text="Reset",command=reset)
running_total = Label(win,text="Score: 0/0")


random_index = random.randint(0,len(answers))
display_word.config(text=anagram_list[random_index])



title.pack()
display_word.pack()
answer_box.pack()
submit_but.pack()
reset_but.pack()
running_total.pack()

win.mainloop()
