from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Memorizer")
window.geometry("600x400")

def open():
    file = askopenfile(title="open file")
    if file is not None:
        listbox.delete(0,END)
        items = file.readlines()
        print(items)
        for item in items:
            listbox.insert(END,item)

def add():
    file_name = enter.get()
    listbox.insert(END,file_name)
    enter.delete(0,END)

def delete():
    chosen_file = listbox.curselection()
    listbox.delete(chosen_file)

def save():
    file = asksaveasfile(defaultextension=".txt")
    if file is not None:
        for item in listbox.get(0,END):
            print(item,file=file)
    listbox.delete(0,END)


enter = Entry(window,width=40)
enter.pack(side=TOP,padx=10,pady=10)
add = Button(window,text="ADD",width=20,height=2,command=add)
add.pack(side=TOP,pady=10,padx=10)

open = Button(window,text="OPEN",width=20,height=2,command=open)
open.pack(side=TOP,padx=10,pady=10)
delete = Button(window,text="DELETE",width=20,height=2,command=delete)
delete.pack(side=TOP,padx=10,pady=10)
save = Button(window,text="SAVE",width=20,height=2,command=save)
save.pack(side=TOP,pady=10,padx=10)

frame = Frame(window)
scroll = Scrollbar(frame,orient="vertical")
scroll.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,width=250,height=200,yscrollcommand=scroll.set,bg="light grey",font=("Aerial",14))
for i in range(1,51):
    listbox.insert(END,"List" + str(i))
listbox.pack(side=LEFT,pady=75)
scroll.config(command=listbox.yview)
frame.pack(side=BOTTOM,padx=125,pady=100)



window.mainloop()