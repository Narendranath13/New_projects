import random
from tkinter import *
from tkinter import messagebox
import pyperclip as pyperclip
top = Tk()
top.geometry("560x480")
top.title('Password Generator & checker')
passw_var=StringVar()

def auto():
    try:
        leng = int(entry1.get())
        if leng >= 8:
            num = chr(random.randint(48, 57))  # ascii value of numbers
            cap = chr(random.randint(65, 90))  # ascii value of uppercase
            sml = chr(random.randint(97, 122))  # ascii value of lowercase
            sym = chr(random.randint(33, 47))  # ascii value of symbols
            gen_pass = cap + num + sym + sml
            rng = leng - 4
            for c in range(rng):
                gen_pass = gen_pass + (chr(random.randint(33, 126)))
            gen_password = ''.join(random.sample(gen_pass, leng))
            passw_var.set(gen_password)
        else:
            messagebox.showwarning("showwarning","please enter the length greater than 8.")
            reset_fields()
    except ValueError:
        messagebox.showerror("showerror", "Please fill the required fields")

def copy():
    gen_pass=passw_var.get()
    pyperclip.copy(gen_pass)

def reset_fields():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    lab.config(text=" ")


def checker():
    temp = entry2.get()
    length=int(len(temp))
    up=0
    lw=0
    syb=0
    nm=0
    global lab
    if(length>=8):
        for i in range(length):
            if(temp[i].isupper()==1):
                up+=1
            if(temp[i].islower()==1):
                lw+=1
            if(     (ord(temp[i])>=33 and ord(temp[i])<=47) or
                    (ord(temp[i])>=58 and ord(temp[i])<=64) or
                    (ord(temp[i])>=91 and ord(temp[i])<=96) or
                    (ord(temp[i])>=123 and ord(temp[i])<=126)):
                syb+=1
            if(ord(temp[i])>=48 and ord(temp[i])<=57):
                nm+=1
        if(nm!=0 and syb!=0 and up!=0 and lw!=0):
            lab=Label(top,text="Your password is strong.",fg="red")
            lab.pack(pady=3)
        elif (nm == 0 or syb == 0 or up == 0 or lw == 0):
            lab=Label(top,text="Your password is Weak.", fg="red")
            lab.pack(pady=3)
    elif(length==0):
        messagebox.showerror("showerror", "Please fill the required fields")
        reset_fields()
    else:
        messagebox.showwarning("showwarning","Your Password is weak.\nLength should me more than 8 characters\nPassword must contain Uppercase,lowercase and symbols.")
        reset_fields()


#labels
Label(top, text="Password Generator", font="Courier 14 bold").pack(pady=20 )
Label(top, text="Enter the lenght").pack(pady=3)
entry1=Entry(top)
entry1.pack()
Button(top, text="Generate",command=auto).pack(pady=5)
entry3=Entry(top, textvariable=passw_var)
entry3.pack()
Button(top, text="Copy password", command=copy).pack()
Label(top, text="Password Strength Checker", font="Courier 12 italic").pack(pady=10)
Label(top, text="Enter your password").pack(pady=3)
entry2=Entry(top)
entry2.pack()
Button(top, text="Check",command=checker).pack(pady=5)
button_reset = Button(top, text="Reset", command=reset_fields)
button_reset.pack()
top.mainloop()


