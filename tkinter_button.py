import tkinter

window = tkinter.Tk()

button = tkinter.Button(window, text="Test button", width=40)
button.pack(padx=10, pady=10)

clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    for click in range(clickCount):
        button.configure(text=f"Click {click}")
    # if clickCount == 1:
    #     button.configure(text="Clik = 1")
    # elif clickCount == 2:
    #     button.configure(text="click = 2")
    # else:
    #     button.pack_forget()

button.bind("<ButtonRelease-1>", onClick)

window.mainloop()