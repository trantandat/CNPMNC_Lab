#Trần Tấn Đạt - 43.01.104.018

from tkinter import *
import random

def calculate(event):
 tx1=int(tx_1.get());
 tx2=int(tx_2.get());
 value1 = random.randrange(tx2 + tx1);
 print(value1)
 updateDisplay1(value1);	
def updateDisplay1(myString):
	displayVariable1.set(myString)

root=Tk()
root.geometry("800x400")
root.title("Predicting percent of loving")
root.grid()

lbl1=Label(root, text="Your name: ", font=("TimeNewRoman",20))
lbl1.pack()
tx_1= Entry(root, width=30, font=("TimeNewRoman",20))
tx_1.pack()

lbl2=Label(root, text="Your girl friend name: ", font=("TimeNewRoman",20))
lbl2.pack()
tx_2= Entry(root, width=30, font=("TimeNewRoman",20))
tx_2.pack()

button_1 = Button(root, text="Start!!", font=("TimeNewRoman",30,"bold"), bg="cyan", fg="blue") 
button_1.bind("<Button-1>", calculate)
button_1.pack()

lbl2=Label(root, text="Percent of your love: ", font=("TimeNewRoman",20))
lbl2.pack()

displayVariable1 = StringVar()
displayLabel1 = Label(root, textvariable=displayVariable1, font=("TimeNewRoman",20))
displayLabel1.pack()

root.mainloop()