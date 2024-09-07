from tkinter import *

window = Tk()
window.title("colours")

def add():
    entered_colour = enter.get()
    listbox.insert(END,entered_colour)

def change():
    chosen_colour = listbox.curselection()
    colour = listbox.get(chosen_colour)
    window.config(background=colour)




adds = Button(window,text="add",width=20,height=2,command=add)
adds.place(x=1200,y=100)

change_colour = Button(window,text="change colour",width=20,height=2,command=change)
change_colour.place(x=1200,y=150)

enter = Entry(window,width=20)
enter.place(x=1200,y=50,height=20)

listbox = Listbox(window,width=100,height=50,font=("aerial",14))
listbox.place(x=50,y=50)
colours = ["red","orange","yellow","green","blue","indigo","violet"]
for i in colours:
    listbox.insert(END,i)




window.mainloop()