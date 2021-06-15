# GUI on tkinter
# графический интерфейс на TKINTER
import my_films
from tkinter import *
from tkinter import messagebox


# main window
# главное окно
root = Tk()
films = my_films.MyFilms()

# общий контент
# изменяемый в зависимости от поиска по названию
CONTENT = films.allFilms()

# main window`s settings
# настройки главного окна
root.title('MY FILMS app GUI')
root.geometry('800x600') # размер
root.resizable(False, False) # неизменяемый размер

# left side
# левая сторона интерфейса
# выбор и поиск контента по алфавиту
left_frame = Label(relief='sunken')

# radio area
# кнопки переключения контента между фильмами и сериалами
def radio_inspect():
    turn_content(radio_var.get())

radio_var = BooleanVar()
radio_var.set(False)# по умолчанию в режиме фильмов

radio1 = Radiobutton(
    left_frame,
    text='FILMS',
    variable=radio_var,
    value=False,
    command=radio_inspect,
    font=('', 10)).place(x=0, y=0, width=195, height=30)
radio2 = Radiobutton(
    left_frame,
    text='SERIALS',
    variable=radio_var,
    font=('', 10),
    command=radio_inspect,
    value=True).place(x=200, y=0, width=195, height=30)

# search area
# поле ввода поиска по буквам или части названия (от начала)
search_title = Label(
    left_frame,
    text='SEARCH',
    font = ('', 10, 'bold'),
    justify=LEFT).place(x=0, y=40, width=395, height = 30)

search_entry = Entry(left_frame)
# функция которая ищет совпадение вводимой строки
# и начала названия фильма
# вводимы строки не зависят от регистра
def search_content(event):
    global CONTENT
    content = search_entry.get()
    CONTENT = [films.allFilms(), films.allSerials][radio_var.get()]
    if content:
        search_list = list([x for x in CONTENT if x[:len(content)].lower() == content])

        if list_box:
            list_box.delete(0, END)
        for x in search_list:
            x = '%s. %s' % ((search_list.index(x))+1, x)
            list_box.insert(END, x)
        CONTENT = search_list.copy()
    else:
        turn_content(radio_var.get())

# функция реагирует на событие нажатия клавиши "ENTER"
search_entry.bind('<Return>', search_content)
search_entry.place(x=10, y=80, width=380, height=30)


# list area
# список всего контента
list_title = Label(
    left_frame,
    text='CHOOSE FILM or SERIAL',
    font = ('', 10, 'bold'),
    justify=LEFT)
list_title.place(x=0, y=120, width=395, height = 30)

# возможность скролить список и в длину и в ширину
scroll_listY = Scrollbar(left_frame)
scroll_listX = Scrollbar(left_frame)

list_box = Listbox(
    left_frame,
    yscrollcommand=scroll_listY.set,
    xscrollcommand=scroll_listX.set,
    font= ('', 9)
)

# отображение информации выбранного контента
# отображение происходит в правой стороне интерфейса
def print_info(event):
    global title_form
    global CONTENT
    # ЕСЛИ ВЫБРАН ФИЛЬМ
    if radio_var.get() == 0:
        
        content = CONTENT[list_box.curselection()[0]]
        director = films.films[content]['dir']
        year = films.films[content]['year']
        rate = films.rate(films.films[content]['rate'])
        rate_num = films.films[content]['rate']

        # цикл для переносов длиных названий
        if len(content) > 24:
        
            last_index = 0
            for x in range(len(content[0:24])):
                if content[x] == ' ':
                    last_index = x

            content = content[0:last_index] + '\n' + content[last_index+1:]

        # цикл для переносов длиных оценок
        if len(rate) > 24:
        
            last_index_rate = 0
            for x in range(len(rate[0:24])):
                if rate[x] == ' ':
                    last_index_rate = x

            rate = rate[0:last_index_rate] + '\n' + rate[last_index_rate+1:]
        
        title_form.destroy()
        title_form = Canvas(right_frame)
        title_form.place(x=5, y=15, width=400, height=600)

        title_form.create_text(15, 0, text='НАЗВАНИЕ ФИЛЬМА:', anchor='nw', font=('', 7, 'bold'))
        title_form.create_text(15, 40, text=content, anchor='nw')
        title_form.create_text(15, 130, text='РЕЖИССЕР ФИЛЬМА:', anchor='nw', font=('', 7, 'bold'))
        title_form.create_text(15, 170, text=director, anchor='nw')
        title_form.create_text(15, 260, text='ГОД ВЫПУСКА:', anchor='nw', font=('', 7, 'bold'))
        title_form.create_text(15, 300, text=year, anchor='nw')
        title_form.create_text(15, 390, text='МОЯ ОЦЕНКА ФИЛЬМУ:', anchor='nw', font=('', 7, 'bold'))
        title_form.create_text(15, 430, text=rate, anchor='nw')

        def press_edit_film():
            a = messagebox.askyesno(
                'ВНИМАНИЕ',
                message='Ты точно хочешь\nИЗМЕНИТЬ информацию?')
            if a == YES:
                # всплывающее окно
                newWin = Toplevel()
                newWin.title('Изменение информации о фильме')
                newWin.geometry('800x360')
                newWin.resizable(False, False)
               
                title_label = Label(newWin, text='Название фильма').pack(fill='x')
                title_entry = Entry(newWin)
                title_entry.insert(0, content)
                title_entry.pack(fill='x', padx=15)
                dir_label = Label(newWin, text='Режиссер фильма').pack(fill='x')
                dir_entry = Entry(newWin)
                dir_entry.insert(0, director)
                dir_entry.pack(fill='x', padx=15)
                year_label = Label(newWin, text='Год выпуска').pack(fill='x')
                year_entry = Entry(newWin)
                year_entry.insert(0, year)
                year_entry.pack(fill='x', padx=15)
                rate_label = Label(newWin, text='Рейтинг фильма').pack(fill='x')
                rate_entry = Entry(newWin)
                rate_entry.insert(0, rate_num)
                rate_entry.pack(fill='x', padx=15)

            
                def save_button():
                    del films.films[content]
                    films.newFilm(
                        title_entry.get(),
                        dir_entry.get(),
                        int(year_entry.get()),
                        int(rate_entry.get()))
                    films.saveFilm()
                    turn_content(radio_var.get())
                    newWin.destroy()

                button = Button(newWin, text='Сохранить!', command=save_button).pack(pady=15)

        Button(
            right_frame,
            text='EDIT',
            command=press_edit_film).place(y=540, x=200-75, width=150, height=45)
    
    # ЕСЛИ ВЫБРАН СЕРИАЛ
    elif radio_var.get() == 1:
        content = CONTENT[list_box.curselection()[0]]
        
        title_form.destroy()
        title_form = Canvas(right_frame)
        title_form.place(x=5, y=15, width=400, height=600)

        title_form.create_text(15, 0, text='НАЗВАНИЕ СЕРИАЛА:', anchor='nw', font=('', 7, 'bold'))
        title_form.create_text(15, 40, text=content, anchor='nw')
        def press_edit_serial():
            a = messagebox.askyesno(
                'ВНИМАНИЕ',
                message='Ты точно хочешь\nИЗМЕНИТЬ информацию?')
            if a == YES:
                # всплывающее окно
                newWin = Toplevel()
                newWin.title('Изменение информации о сериале')
                newWin.geometry('800x360')
                newWin.resizable(False, False)

                title_label = Label(newWin, text='Название сериала').pack(fill='x')
                title_entry = Entry(newWin)
                title_entry.insert(0, content)
                title_entry.pack(fill='x', padx=15)
                def save_button():
                    films.allSerials.remove(content)
                    films.newSerial(title_entry.get())
                    films.saveSerials()
                    turn_content(radio_var.get())
                    newWin.destroy()
                button = Button(newWin, text='Сохранить!', command=save_button).pack(pady=15)
        Button(
            right_frame,
            text='EDIT',
            command=press_edit_serial).place(y=540, x=200-75, width=150, height=45)
        
    else:
        pass

list_box.bind('<Double-Button-1>', print_info)

scroll_listY.config(command=list_box.yview)
scroll_listX.config(command=list_box.xview, orient='horizontal')

list_box.place(x=10, y=150, width=360, height = 350)

scroll_listY.place(x=370, y=150, width=20, height=350)
scroll_listX.place(x=10, y=500, height=20, width=380)

def turn_content(content):
    global CONTENT
    CONTENT = [films.allFilms(), films.allSerials][radio_var.get()]
    all_list = [films.allFilms(), films.allSerials]
    if list_box:
        list_box.delete(0, END)
    content_list = all_list[content]
    for x in content_list:
        x = '%s. %s' % ((content_list.index(x))+1, x)
        list_box.insert(END, x)
    

turn_content(radio_var.get())

left_frame.place(x=0, y=0, width=400, height=600)

# button ADD
def press_add():
    a = messagebox.askyesno(
        'ВНИМАНИЕ',
        message='Ты точно хочешь\nДОБАВИТЬ фильм/сериал?')
    if a == YES:
        # всплывающее окно
        newWin = Toplevel()
        newWin.title('Добавление нового фильма или сериала')
        newWin.geometry('800x360')
        newWin.resizable(False, False)
        if radio_var.get() == 0:
            title_label = Label(newWin, text='Название фильма').pack(fill='x')
            title_entry = Entry(newWin)
            title_entry.pack(fill='x', padx=15)
            dir_label = Label(newWin, text='Режиссер фильма').pack(fill='x')
            dir_entry = Entry(newWin)
            dir_entry.pack(fill='x', padx=15)
            year_label = Label(newWin, text='Год выпуска').pack(fill='x')
            year_entry = Entry(newWin)
            year_entry.pack(fill='x', padx=15)
            rate_label = Label(newWin, text='Рейтинг фильма').pack(fill='x')
            rate_entry = Entry(newWin)
            rate_entry.pack(fill='x', padx=15)

            
            def save_button():
                films.newFilm(
                    title_entry.get(),
                    dir_entry.get(),
                    int(year_entry.get()),
                    int(rate_entry.get()))
                films.saveFilm()
                turn_content(radio_var.get())
                newWin.destroy()

            button = Button(newWin, text='Сохранить!', command=save_button).pack(pady=15)

        elif radio_var.get() == 1:
            title_label = Label(newWin, text='Название сериала').pack(fill='x')
            title_entry = Entry(newWin)
            title_entry.pack(fill='x', padx=15)
            def save_button():
                films.newSerial(title_entry.get())
                films.saveSerials()
                turn_content(radio_var.get())
                newWin.destroy()
            button = Button(newWin, text='Сохранить!', command=save_button).pack(pady=15)
        else:
            pass    

    else:
        pass

Button(
    left_frame,
    text='ADD',
    command=press_add).place(y=540, x=200-75, width=150, height=45)

# right side
right_frame = Frame()



#
title_form = Canvas(right_frame)
title_form.create_text(
    200,
    15,
    text='Описание фильма\nили сериала',
    font=('', 10, 'bold'),
    anchor='n',
    justify='center')

title_form.place(x=5, y=40, width=400, height=160)
right_frame.place(x=400, y=0, width=400, height=600)

# исполняющий цикл
root.mainloop()