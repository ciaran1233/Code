from tkinter import *
from tkinter import ttk
from webbrowser import *


lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + converter.winfo_x(), event.y - lastClickY + converter.winfo_y()
    converter.geometry("+%s+%s" % (x , y))


converter = Tk()
converter.title("Currency Converter")
converter['bg'] = 'black'
converter.resizable(False, False)
converter.overrideredirect(True)
converter.attributes('-topmost', True)
converter.geometry("600x400+500+250")
converter.bind('<Button-1>', SaveLastClickPos)
converter.bind('<B1-Motion>', Dragging)




OPTIONS = {
    "Australian Dollar ($ AUD)": 1.81,
    "Brazilian Real (R$ BRL)": 6.14,
    "Canadian Dollar ($ CAD)": 1.58,
    "Chinese Yuan (¥ CNY)": 8.45,
    "Danish Krone (Kr DKK) ": 8.68,
    "Euro (€ EUR)": 1.17,
    "Hong Kong Dollar (HK$ HKD)": 9.10,
    "Indian Rupee (₹ INR)": 95.58,
    "Japanese Yen ( ¥ JPY)": 171.39,
    "Norwegian Krone (Kr NOK)": 12.02,
    "South African Rand (R ZAR)": 21.17,
    "Swiss Franc (₣ CHF)": 1.16,
    "Ukrainan Hryvnia (₴ UAH)": 42.79,
    "US Dollar ($ USD)": 1.16
}


def ok():
    result.config(state='normal')
    price = pounds.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer, None)
    converted = round(float(DICT) * int(price), 2)
    result.delete(1.0, END)
    result.tag_configure("center", justify='center')
    result.insert(INSERT, "Price in ", INSERT, answer, INSERT, " = ", INSERT, converted, INSERT, "\nExchange Rate: ", INSERT, DICT)
    result.tag_add("center", 1.0, "end")
    result.config(state='disabled')


def clear():
    result.config(state='normal')
    result.delete(1.0, END)
    pounds.delete(0, END)
    variable1.set("Select an Currency")
    result.config(state='disabled')

    
appName = Label(converter, text="Exchange Rate Calculator", font=("MS Gothic", 25, "bold", "underline"), fg="red", bg='black', justify=CENTER)
appName.place(x=80, y=10)

exit_Button=Button(converter, text='X', fg='red', command=converter.destroy)
exit_Button.place(x=580, y=0)

result = Text(converter, height=2, width=35, font=("arial", 12, "bold"), bd=5)
result.config(state='disabled')
result.pack()
result.place(x=130, y=60)

amount = Label(converter, text="Please type an amount in £", font=("MS Gothic", 12, "bold"), fg="red", bg="black")
amount.place(x=170, y=130)

pounds = Entry(converter, font=("arial", 13))
pounds.place(x=185, y=170, width=200)


variable1 = StringVar(converter)
variable1.set("Select an Currency")
option = OptionMenu(converter, variable1, *OPTIONS)
option.config(font=("MS Gothic", 15, "bold"), fg="white", bg="red", activebackground='white', activeforeground='black')
option.place(x=115, y=225, width=325, height=40)

menu = converter.nametowidget(option.menuname)
menu.config(font=("MS Gothic", 16), fg="white", bg="black", activebackground='white', activeforeground='black')

convertButton = Button(converter, text="Convert", fg="white", font=("MS Gothic", 16), bg="red", activebackground='white', activeforeground='black', command=ok)
convertButton.place(x=140, y=300, height=40, width=150)

clearButton = Button(converter, text="Clear", fg="white", font=("MS Gothic", 16), bg="red", activebackground='white', activeforeground='black', command=clear)
clearButton.place(x=335, y=300, height=40, width=100)


converter.mainloop()
