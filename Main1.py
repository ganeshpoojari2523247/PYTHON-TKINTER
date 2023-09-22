from  tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Project")
root.geometry("300x200+0+0")
root.resizable(False,False)

label1=Label(root,text="Name:",font=("Arial",10,"bold"),padx=10,pady=10)
label1.grid(row=0,column=0)
ent=Entry(root,font=("Arial",10,"bold"))
ent.grid(row=0,column=1)

label2=Label(root,text=" Email id:",font=("Arial",10,"bold"),padx=10,pady=10)
label2.grid(row=1,column=0)
ent2=Entry(root,font=("Arial",10,"bold"))
ent2.grid(row=1,column=1)

label3=Label(root,text="Password",font=("Arial",10,"bold"),padx=10,pady=10)
label3.grid(row=2,column=0)
ent3=Entry(root,font=("Arial",10,"bold"))
ent3.grid(row=2,column=1)









def nextpage():
    nextpage=Toplevel(root)
    nextpage.title("Home")
    nextpage.geometry("1000x800+0+0")
    nextpage.resizable(False,False)




btn=Button(root,text="ENTER",font=("Arial",10,"bold"),command=nextpage)
btn.place(x=130,y=120)








root.mainloop()
