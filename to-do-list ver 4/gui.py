import tkinter
from tkinter import *
from tkinter import ttk

window = tkinter.Tk()
window.title("new project")

frame = tkinter.Frame(window)
frame.pack()

#First Frame
date_frame = tkinter.LabelFrame(frame, text= "date format: (dd/mm/yyyy)")
date_frame.grid(row=0, column=1, padx=20, pady=10)

date_label = tkinter.Label(date_frame, text="Date")
date_label.grid(row=0, column=0)
date_spinbox = tkinter.Spinbox(date_frame, from_= 1, to= 31)
date_spinbox.grid(row=1, column=0)

month_label = tkinter.Label(date_frame, text="Month")
month_label.grid(row=0, column=1)
month_combobox = ttk.Combobox(date_frame, values=[
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP",
    "OCT", "NOV", "DEC"
])
month_combobox.grid(row=1, column=1)

year_label = tkinter.Label(date_frame, text="Year")
year_label.grid(row=0, column=2)
year_spinbox = tkinter.Spinbox(date_frame, from_= 2023, to= 3000)
year_spinbox.grid(row=1, column=2)

submit_button = tkinter.Button(date_frame, text="Submit")
submit_button.grid(row=1, column=3)

for widget in date_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Second Frame
ask_frame = tkinter.LabelFrame(frame, text="click 'yes' or 'no'")
ask_frame.grid(row=1, column=1, sticky="news", padx=20, pady=10)

ask_user_label = tkinter.Label(ask_frame, text="Do You Want "
                            "To Change Your List?")
ask_user_label.grid(row=0, column=0)

yes_button = tkinter.Button(ask_frame, text="YES",
                            width=15)
yes_button.grid(row=1, column=0)

no_button = tkinter.Button(ask_frame, text="NO",
                        width=15)
no_button.grid(row=1, column=1)

for widget in ask_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Third Frame
add_list_frame = tkinter.LabelFrame(frame, text="type your new "
                                    "list inside the box")
add_list_frame.grid(row=2, column=1, sticky="news", padx=20, pady=10)

user_input = tkinter.Entry(add_list_frame, width=80)
user_input.grid(row=1, column=0)

add_list_label = tkinter.Label(add_list_frame, text="Add New List: ")
add_list_label.grid(row=0, column=0)

add_button = tkinter.Button(add_list_frame, text="ADD")
add_button.grid(row=0, column=1)
submit_button = tkinter.Button(add_list_frame, text="Submit")
submit_button.grid(row=1, column=1)

#Fourth Frame
done_frame = tkinter.Button(frame, text="DONE")
done_frame.grid(row=3, column=1, sticky="news", padx=10, pady=5)

#Fifth Frame
display_frame = tkinter.LabelFrame(frame, text= "Display")
display_frame.grid(row=0, column=0, rowspan=4, sticky="news", padx=20, pady=10)

example_label = Text(display_frame, font="consolas 18",
                     bg="#323846", fg="lightgreen")
example_label.grid(row=0, column=0)
example_label.configure(width=40, height=15)

window.mainloop()