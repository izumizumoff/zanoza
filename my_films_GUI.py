# GUI on tkinter
import my_films
from tkinter import *
from tkinter import messagebox
# main window
root = Tk()
films = my_films.MyFilms()
# main window`s settings
root.title('MY FILMS app GUI')
root.geometry('1000x800')
root.resizable(False, False)


# left side
left_frame = Label(relief='sunken')

# radio area
def radio_inspect():
    print(radio_var.get())

radio_var = BooleanVar()
radio_var.set(False)
radio1 = Radiobutton(
    left_frame,
    text='FILMS',
    variable=radio_var,
    value=False,
    command=radio_inspect,
    font=('', 9, 'italic')).place(x=0, y=0, width=245, height=40)
radio2 = Radiobutton(
    left_frame,
    text='SERIALS',
    variable=radio_var,
    font=('', 9, 'italic'),
    command=radio_inspect,
    value=True).place(x=250, y=0, width=245, height=40)

# search area
search_title = Label(
    left_frame,
    text='SEARCH',
    font = ('', 10, 'bold'),
    justify=LEFT).place(x=0, y=50, width=495, height = 40)

search_entry = Entry(left_frame).place(x=10, y=90, width=480, height=40)


# list area
list_title = Label(
    left_frame,
    text='CHOOSE FILM or SERIAL',
    font = ('', 10, 'bold'),
    justify=LEFT)
list_title.place(x=0, y=140, width=495, height = 40)


scroll_listY = Scrollbar(left_frame)
scroll_listX = Scrollbar(left_frame)

list_box = Listbox(
    left_frame,
    yscrollcommand=scroll_listY.set,
    xscrollcommand=scroll_listX.set,
    font= ('', 9)
)

scroll_listY.config(command=list_box.yview)
scroll_listX.config(command=list_box.xview, orient='horizontal')

list_box.place(x=10, y=180, width=460, height = 540)

scroll_listY.place(x=470, y=180, width=20, height=540)
scroll_listX.place(x=10, y=720, height=20, width=480)

all_list = films.allFilms()

for x in film_list:
    x = '%s. %s' % ((film_list.index(x))+1, x)
    list_box.insert(END, x)

left_frame.place(x=0, y=0, width=500, height=800)

# button ADD
def press_add():
    a = messagebox.askyesno('ВНИМАНИЕ', message='Ты точно хочешь\nДОБАВИТЬ фильм/сериал?')
    if a == YES:
        messagebox.showwarning(message='Ты хочешь нажать ДА')
        print('yes')
    elif a == NO:
        print('no')
    else:
        pass

Button(left_frame, text='ADD', command=press_add).place(y=745, x=150, width=200, height=45)

# right side
right_frame = Label()

right_frame.place(x=500, y=0, width=500, height=800)

#
root.mainloop()