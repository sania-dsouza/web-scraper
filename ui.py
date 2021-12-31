from tkinter import *
from tkinter import ttk
from main import *

window = Tk()
window.title('Scrappit')
window.geometry("190x50")
window.configure(bg='green')

mainframe = ttk.Frame(window)

ttk.Button(window, text="Get CSV", command=main).grid(column=2, row=1)
ttk.Button(window, text="Quit", command=window.destroy).grid(column=4, row=1)

# ttk.Label(window, text="The CSV results are downloaded").grid(column=1, row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.quit()
window.mainloop()