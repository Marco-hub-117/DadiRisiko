from tkinter import *
import random

root=Tk()
root.title("Roll Dice")
root.geometry("500x400")

Label=Label(root,font=('helvetica' , 150 ,'bold' ),text='')
Label.pack()
def rolldice():
    dice=['\u2680','\u2681', '\u2682','\u2683','\u2684','\u2685']
    Label.configure(text=f'{random.choice(dice)}')
    Label.pack()

button=Button(root,font=('helvetica',25),text='Roll Dice',bg="blue",command=rolldice)
button.pack()
root.mainloop()