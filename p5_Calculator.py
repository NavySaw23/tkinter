from tkinter import *

root = Tk()
root.title("Calculator Shell")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Button Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    firstNumber = e.get()     # Puts input from "e" into a variable
    global f_num
    global math 
    math = "addition"
    f_num = int(firstNumber)  # typecasting to int
    e.delete(0, END)          # Emptying the insert field

def button_substract():
    firstNumber = e.get()     
    global f_num
    global math 
    math = "substraction"
    f_num = int(firstNumber)  
    e.delete(0, END)          

def button_multiply():
    firstNumber = e.get()     
    global f_num
    global math 
    math = "multiplication"
    f_num = int(firstNumber)  
    e.delete(0, END)          

def button_divide():
    firstNumber = e.get()     
    global f_num
    global math 
    math = "division"
    f_num = int(firstNumber)  
    e.delete(0, END)          

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, f_num+int(second_number))
    if math=="substraction":
        e.insert(0, f_num-int(second_number))
    if math=="multiplication":
        e.insert(0, f_num*int(second_number))
    if math=="division":
        e.insert(0, f_num/int(second_number))


# Defining buttons
button1 = Button(root, text="1", command=lambda: button_click(1), padx=40, pady=20) #Need to use Lambda: when passing arguments
button2 = Button(root, text="2", command=lambda: button_click(2), padx=40, pady=20)
button3 = Button(root, text="3", command=lambda: button_click(3), padx=40, pady=20)
button4 = Button(root, text="4", command=lambda: button_click(4), padx=40, pady=20)
button5 = Button(root, text="5", command=lambda: button_click(5), padx=40, pady=20)
button6 = Button(root, text="6", command=lambda: button_click(6), padx=40, pady=20)
button7 = Button(root, text="7", command=lambda: button_click(7), padx=40, pady=20)
button8 = Button(root, text="8", command=lambda: button_click(8), padx=40, pady=20)
button9 = Button(root, text="9", command=lambda: button_click(9), padx=40, pady=20)
button0 = Button(root, text="0", command=lambda: button_click(0), padx=40, pady=20)

buttonAdd = Button(root, text="+", command=button_add, padx=39, pady=20)
buttonSub = Button(root, text="-", command=button_substract, padx=41, pady=20)
buttonMul = Button(root, text="*", command=button_multiply, padx=41, pady=20)
buttonDiv = Button(root, text="/", command=button_divide, padx=41, pady=20)

buttonClear = Button(root, text="Clear", command=button_clear, padx=85, pady=20)
buttonEqual = Button(root, text="=", command=button_equal, padx=95, pady=20)


# Grid setup
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button0.grid(row=4,column=0)
buttonClear.grid(row=4, column=1, columnspan=2)

buttonAdd.grid(row=5, column=0)
buttonMul.grid(row=5, column=1)
buttonDiv.grid(row=5, column=2)

buttonSub.grid(row=6, column=0)
buttonEqual.grid(row=6, column=1, columnspan=2)

root.mainloop()