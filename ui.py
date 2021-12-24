from tkinter import *
from tkinter import ttk
import main

window = Tk()
window.title('Scrappit')
window.geometry("400x80")
window.configure(bg='pink')

mainframe = ttk.Frame(window, padding="20 20 20 20")

ttk.Label(window, text="Topic could be any of \"job\", etc").grid(column=2, row=0)
ttk.Label(window, text="Enter the topic ").grid(column=1, row=1)

topic = StringVar()
topic_entry = ttk.Entry(window, width=20, textvariable=topic)
topic_entry.grid(column=2, row=1)

ttk.Button(window, text="Get CSV").grid(column=1, row=3)
# ttk.Button(window, text="Get CSV", command=main).grid(column=1, row=3)

# ttk.Label(window, text="The CSV results are downloaded").grid(column=1, row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

topic_entry.focus()
window.bind("<Return>")


window.mainloop()