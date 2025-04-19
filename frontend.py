from tkinter import *
from tkinter import messagebox
import Create
import Read
import Delete
import table
import Search
import update
import delete2
import excel
from PIL import Image,ImageTk
import datetime
import pathlib


# ===============================system=======================================

root =Tk()
root.title('Data Base')
root.geometry('470x250')
root.resizable(width=False , height=False)

# ================================entry=======================================

in1 = Entry(root , bg='powder blue')
in2 = Entry(root , bg='powder blue')
in3 = Entry(root , bg='powder blue')
in4 = Entry(root , bg='powder blue')
in1.grid(row = 0 , column= 1)
in2.grid(row = 0 , column= 3)
in3.grid(row = 1 , column= 1)
in4.grid(row = 1 , column= 3)

# ================================Label=======================================

lb1 = Label(root , text='Name :')
lb2 = Label(root , text='Family :')
lb3 = Label(root , text='Tell :')
lb4 = Label(root , text='National code :')
lb1.grid(row = 0 ,column=0 , padx= 2 , pady= 2)
lb2.grid(row = 0 ,column=2 , padx= 2 , pady= 2)
lb3.grid(row = 1 ,column=0 , padx= 2 , pady= 2)
lb4.grid(row = 1 ,column=2 , padx= 2 , pady= 2)
# img = image.img.resize((70 , 70))
# img = ImageTk.PhotoImage(img)
# lb_pic = Label(root , image=img , width=70 , height=70)
# lb_pic.grid(row=0 , column=4 ,rowspan=2)

# ================================listbox=====================================

l1 = Listbox(root , width=57 )
l1.grid(row = 2 , column= 1 , columnspan=3 , rowspan=7 )

# ===============================scrollbar====================================

sb1 = Scrollbar(root)
sb1.grid( row= 2 , column= 0 , rowspan=3)
l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview)

# =================================connect=====================================

def get_selected(event) :
    if len(l1.curselection()) > 0 :
        global selected_user
        index = l1.curselection()[0]
        selected_user = l1.get(index)
        in1.delete(0 , END)
        in1.insert(END , selected_user[1])
        in2.delete(0 , END)
        in2.insert(END , selected_user[2])
        in3.delete(0 ,END)
        in3.insert(END , selected_user[3])
        in4.delete(0 , END)
        in4.insert(END , selected_user[4])

l1.bind('<<ListboxSelect>>' , get_selected)

def clr_entry() :
    in1.delete(0 , END)
    in2.delete(0 , END)
    in3.delete(0 , END)
    in4.delete(0 , END)

def creat() :
    Create.add(in1.get() , in2.get() , in3.get() , in4.get())
    users = Read.user_List('i')
    for user in users :
        pass
    l1.insert(END , user)
    excel.export()
    clr_entry()
    

def clr_scrn():
    l1.delete(0 ,END)

def search() :
    clr_scrn()
    users = Search.search(in1.get() , in2.get() , in3.get() , in4.get())
    for user in users :
        l1.insert(END , user)
    clr_entry()


def List() :
    clr_scrn()
    users = Read.user_List('i')
    for user in users :
        l1.insert(END , user)
    clr_entry()

def delete() :
   delete = Delete.delete(selected_user[0])
   #delete1 = delete2.delete(in1.get() , in2.get() , in3.get() , in4.get())
   l1.insert(END , delete)
   #l1.insert(END , delete1)
   List()
   excel.export()
   clr_entry()

def upd() :
    up = update.update(in1.get() , in2.get() , in3.get() , in4.get() , selected_user[0])
    l1.insert(END ,up)
    List()
    excel.export()
    clr_entry()


# =================================button=====================================

btn = Button(root , text='ADD' , background='gray' ,width=6 , height=1 , command=lambda:creat())
btn1 = Button(root , text='LIST' , background='gray' , width=6 , height=1 , command=List)
btn2 = Button(root , text='SEARCH' , background='gray' , width=6 , height=1 , command=lambda:search())
btn3 = Button(root , text='DELETE' , background='gray' , width=6 , height=1 , command=delete)
btn4 = Button(root , text='UPDATE' , background='gray' , width=6 , height=1 , command=upd)
btn5 = Button(root , text='CLOSE' , background='gray' , width=6 , height=1 , command=root.destroy)
btn.grid(row = 2 , column=4  ,pady=1 , padx=2)
btn1.grid(row = 3 , column=4  ,pady=1 , padx=2)
btn2.grid(row = 4 , column=4  ,pady=1 , padx=2)
btn3.grid(row = 5 , column=4  , pady=1 , padx=2)
btn4.grid(row = 6 , column=4  , pady=1 , padx=2)
btn5.grid(row = 7 , column=4  , pady=1 , padx=2)


root.mainloop()