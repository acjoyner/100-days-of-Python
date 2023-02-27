import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)

#Label
my_label = tkinter.Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0,row=0)

#Button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)
button = tkinter.Button(text="Click Me Again", command=button_clicked)
button.grid(column=2,row=0)

#Entry
input = tkinter.Entry(width=10)
input.get()
input.grid(column=2,row=2)


window.mainloop()




