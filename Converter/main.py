from tkinter import *
import ctypes
from tkinter.ttk import Combobox
import requests

# Enable high-DPI scaling
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Window setup
window = Tk()
window.minsize(800,500)
window.title("Currency Converter")

# Title
my_label = Label(text="CURRENCY CONVERTER",font=("Courier",20,'bold'))
my_label.place(x=160,y=0)

# Amount label and input
amount = Label(text="Amount: ",font=("Courier",18,'bold'))
amount.place(x=100,y=80)
amt_input = Entry(width=15)
amt_input.place(x=300,y=90)

# Currency list
CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

# Function to get live rate
def get_live_rate(from_curr, to_curr):
    if from_curr == to_curr:
        return 1.0
    url = f"https://api.frankfurter.app/latest?from={from_curr}&to={to_curr}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][to_curr]

# Convert button action
def convert():
    try:
        amount = float(amt_input.get())
        from_currency = combo.get()
        to_currency = combo2.get()

        rate = get_live_rate(from_currency, to_currency)
        result = amount * rate

        # Display result
        text.delete('1.0', END)
        text.insert(END, f"{result:.2f}")
    except Exception as e:
        text.delete('1.0', END)
        text.insert(END, "Error: Check input or connection")

# From Currency
frm_currency = Label(text="From Currency: ", font=("Courier", 18, 'bold'))
frm_currency.place(x=100, y=130)
combo = Combobox(window, values=CurrencyCode_list, state="readonly")
combo.place(x=450, y=140)
combo.current(1)  # Default: USD

# To Currency
to_currency = Label(text="To Currency: ", font=("Courier", 18, 'bold'))
to_currency.place(x=100, y=190)
combo2 = Combobox(window, values=CurrencyCode_list, state="readonly")
combo2.place(x=450, y=200)
combo2.current(0)  # Default: INR

# Convert Button
button = Button(text="CONVERT", command=convert)
button.config(width=15)
button.place(x=310, y=280)

# Result Display
con_currency = Label(text="Converted Amount: ", font=("Courier", 18, 'bold'))
con_currency.place(x=100, y=350)
text = Text(width=15, height=1.2)
text.place(x=500, y=360)

# Creator Label
creator_label = Label(window,
                      text="created by Sriram Bharath ^^",
                      font=("Helvetica", 9, "italic"),
                      fg="#888888",     # soft gray text
                      bg=window["bg"])  # same as window background
creator_label.pack(side="bottom", pady=5)

# Run the app
window.mainloop()
