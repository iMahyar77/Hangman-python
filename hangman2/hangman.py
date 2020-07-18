from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk

root = Tk()
root.resizable(False, False)
names = ["UMBRELLA", "APPLE", "CONFIGURE", "BIRD", "BEAUTY", "TEACHER", "PYTHON", "DONE", "END"]
randomName = random.choice(names)
list1 = []
randomLen = len(randomName)

for j in range(len(randomName)):
    list1.append(" _ ")
str1 = "".join(list1)
list2 = list(randomName)
lives = 8

# INSERTING IMAGES
imagePath = ["Lives0.jpg", "Lives1.jpg", "Lives2.jpg", "Lives3.jpg", "Lives4.jpg", "Lives5.jpg", "Lives6.jpg",
             "Lives7.jpg", "Lives8.jpg"]
img = Image.open(imagePath[lives])
img = ImageTk.PhotoImage(img)


def switch(x):
    m = 0
    global lives
    if lives > 0:
        for i in range(randomLen):
            if x == list2[i]:
                list1[i] = x
                m += 1
        str3 = "".join(list1)
        label1.config(text=str3, font=('Arial', '30'))
    if list1 == list2:
        messagebox.showinfo("Congrats!", "YOU WIN")
        root.destroy()
    if m == 0:
        lives -= 1
        image = Image.open(imagePath[lives])
        imageNew = ImageTk.PhotoImage(image)
        label2.configure(image=imageNew)
        label2.image = imageNew
        if lives == 0:
            label3 = Label(root, text="Lives:", font=('Arial', '15'))
            label3.place(x=400, y=150)
            label4 = Label(root, text=lives, font=('Arial', '15'))
            label4.place(x=455, y=150)
            messagebox.showerror("BAD LUCK", "YOU LOSE")
            root.destroy()

    label3 = Label(root, text="Lives:", font=('Arial', '15'))
    label3.place(x=400, y=150)
    label4 = Label(root, text=lives, font=('Arial', '15'))
    label4.place(x=455, y=150)


# PUTTING UP THE KEYS
root.title(" HangMan Game ")
root.geometry("885x700")
btn1 = Button(root, text="A", width=3, height=1, font=('Arial', '10'), command=lambda: switch("A"))
btn2 = Button(root, text="B", width=3, height=1, font=('Arial', '10'), command=lambda: switch("B"))
btn3 = Button(root, text="C", width=3, height=1, font=('Arial', '10'), command=lambda: switch("C"))
btn4 = Button(root, text="D", width=3, height=1, font=('Arial', '10'), command=lambda: switch("D"))
btn5 = Button(root, text="E", width=3, height=1, font=('Arial', '10'), command=lambda: switch("E"))
btn6 = Button(root, text="F", width=3, height=1, font=('Arial', '10'), command=lambda: switch("F"))
btn7 = Button(root, text="G", width=3, height=1, font=('Arial', '10'), command=lambda: switch("G"))
btn8 = Button(root, text="H", width=3, height=1, font=('Arial', '10'), command=lambda: switch("H"))
btn9 = Button(root, text="I", width=3, height=1, font=('Arial', '10'), command=lambda: switch("I"))
btn10 = Button(root, text="J", width=3, height=1, font=('Arial', '10'), command=lambda: switch("J"))
btn11 = Button(root, text="K", width=3, height=1, font=('Arial', '10'), command=lambda: switch("K"))
btn12 = Button(root, text="L", width=3, height=1, font=('Arial', '10'), command=lambda: switch("L"))
btn13 = Button(root, text="M", width=3, height=1, font=('Arial', '10'), command=lambda: switch("M"))
btn14 = Button(root, text="N", width=3, height=1, font=('Arial', '10'), command=lambda: switch("N"))
btn15 = Button(root, text="O", width=3, height=1, font=('Arial', '10'), command=lambda: switch("O"))
btn16 = Button(root, text="P", width=3, height=1, font=('Arial', '10'), command=lambda: switch("P"))
btn17 = Button(root, text="Q", width=3, height=1, font=('Arial', '10'), command=lambda: switch("Q"))
btn18 = Button(root, text="R", width=3, height=1, font=('Arial', '10'), command=lambda: switch("R"))
btn19 = Button(root, text="S", width=3, height=1, font=('Arial', '10'), command=lambda: switch("S"))
btn20 = Button(root, text="T", width=3, height=1, font=('Arial', '10'), command=lambda: switch("T"))
btn21 = Button(root, text="U", width=3, height=1, font=('Arial', '10'), command=lambda: switch("U"))
btn22 = Button(root, text="V", width=3, height=1, font=('Arial', '10'), command=lambda: switch("V"))
btn23 = Button(root, text="W", width=3, height=1, font=('Arial', '10'), command=lambda: switch("W"))
btn24 = Button(root, text="X", width=3, height=1, font=('Arial', '10'), command=lambda: switch("X"))
btn25 = Button(root, text="Y", width=3, height=1, font=('Arial', '10'), command=lambda: switch("Y"))
btn26 = Button(root, text="Z", width=3, height=1, font=('Arial', '10'), command=lambda: switch("Z"))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=0, column=3)
btn5.grid(row=0, column=4)
btn6.grid(row=0, column=5)
btn7.grid(row=0, column=6)
btn8.grid(row=0, column=7)
btn9.grid(row=0, column=8)
btn10.grid(row=0, column=9)
btn11.grid(row=0, column=10)
btn12.grid(row=0, column=11)
btn13.grid(row=0, column=12)
btn14.grid(row=0, column=13)
btn15.grid(row=0, column=14)
btn16.grid(row=0, column=15)
btn17.grid(row=0, column=16)
btn18.grid(row=0, column=17)
btn19.grid(row=0, column=18)
btn20.grid(row=0, column=19)
btn21.grid(row=0, column=20)
btn22.grid(row=0, column=21)
btn23.grid(row=0, column=22)
btn24.grid(row=0, column=23)
btn25.grid(row=0, column=24)
btn26.grid(row=0, column=25)

# INSERTING WIDGETS
label1 = Label()
label1.place(x=300, y=50)
label1.config(text=str1, font=('Arial', '30'))

label2 = Label(root, image=img)
label3 = Label(root, text="Lives:", font=('Arial', '15'))
label4 = Label(root, text=lives, font=('Arial', '15'))
label2.place(x=130, y=200)
label3.place(x=400, y=150)
label4.place(x=455, y=150)
root.config(background="light blue")

mainloop()
