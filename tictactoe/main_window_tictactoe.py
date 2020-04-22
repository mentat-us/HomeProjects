from tkinter import *

main_window = Tk()

ok_button = Button(main_window, text="click me")
msg_label = Label(main_window, text="Mesaj")
ok_button.pack()
msg_label.pack()


main_window.mainloop()