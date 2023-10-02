import tkinter

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title('Password Manager')

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=1)

window.mainloop()