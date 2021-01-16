from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("Credit Card Authentication")
root.geometry("700x500")
root.configure(background="#fed700")
entry=Entry(root)
card=ImageTk.PhotoImage(Image.open ("card.png"))
entry.place(relx=0.5,rely=0.3,anchor=CENTER)
label_card=Label(root,image=card)
label_card.place(relx=0.5,rely=0.7,anchor=CENTER)
def authentication():
    card_number=entry.get()
    try:
        int(card_number)
    except(ValueError):
        messagebox.showerror( "Alert","Credit card not accepted.Please put vaild pin code")
    else:
        messagebox.showinfo( "Alert","Credit card accepted")
btn=Button(root,text="Check credit card",command=authentication)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()