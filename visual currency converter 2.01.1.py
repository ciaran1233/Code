from tkinter import *
from tkinter import ttk




converter = Tk()
converter.title("Unit Converter")
converter.geometry("600x400")

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


def clear():
    result.config(state='normal')
    result.delete(1.0, END)
    pounds.delete(0, END)
    variable1.set("Select an Currency")
    result.config(state='disabled')



appName = Label(converter,text="Currency Converter",font=("arial",25,"bold","underline"),fg="light blue")
appName.place(x=60, y=20)

result = Text (converter,height=5,width=30,font = ("arial",15,"bold"),bd=5)
result.place(x=150,y=110)

pounds = Entry(converter, font=("arial",20))
pounds.place(x=170, y=275, width=210)
             

variable1 = StringVar(converter)
variable1.set("select an currency")
option =OptionMenu(converter,variable1, *OPTIONS)
option.config(font=("MS Gothic", 15, "bold"), fg="black", bg="grey", activebackground='white', activeforeground='light blue')
option.place(x=160,y=320,width=240,height=40)



button =Button(converter,text="convert",fg="black",font=("arial",25),bg="powderblue",command=ok)
button.place(x=305,y=360,height=40,width=110)

clearButton = Button(converter, text="Clear", fg="white", font=("MS Gothic", 16), bg="red", activebackground='white', activeforeground='black', command=clear)
clearButton.place(x=190, y=360, height=40, width=100)

converter.mainloop()
        



