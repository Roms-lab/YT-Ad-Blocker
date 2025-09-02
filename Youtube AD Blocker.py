from tkinter import *

print("Blocking Currently Disabled.")

window = Tk()
window.geometry("600x420")
window.title("Youtube AD Blocker")

# Load icon (handle missing file gracefully)
try:
    Icon = PhotoImage(file='logo.png')
    window.iconphoto(True, Icon)
except Exception as e:
    print("Icon not loaded:", e)

window.config(background="black")

Enable_Disable = "Disabled"

def click():
    global Enable_Disable
    if Enable_Disable == "Disabled":
        Enable_Disable = "Enabled"
        label.config(text="Blocking Enabled", fg='green')
    else:
        Enable_Disable = "Disabled"
        label.config(text="Blocking Disabled", fg='red')
    print("Currently", Enable_Disable)

label = Label(window,
              text="Blocking Disabled",
              font=('Arial', 20, 'bold'),
              fg='red',
              bg='black',
              relief='raised',
              bd=10,
              padx=10,
              pady=10)
label.place(x=135, y=75)

button = Button(window,
                text="Enable/Disable Blocker",
                command=click,
                font=('Arial', 20, 'bold'),
                fg='green',
                bg='black',
                relief='raised',
                bd=10,
                padx=10,
                pady=10
                )
button.place(x=100, y=200)

window.mainloop()