import tkinter
import random
from tkinter.scrolledtext import *
from tkinter import *


def start_new_game():  # диалоговое окошко для начала новой игры

    def return_and_die():  # типа начать игру
        global hard_level
        global word_secret
        global word_secret_list
        global flag
        global steps
        global r
        hard_level = hardlist.get()  # устанавливает уровень сложности
        word_secret = num_random(hard_level)
        word_secret_list = list(word_secret)
        mainbox.delete(1.0, END)
        mainbox.configure(fg="black")
        dialog.destroy()  # героически умирает

    dialog = Tk()
    dialog.title("Новая игра")
    label = Label(dialog, text=u"Выберите количество букв в слове:")
    hardlist = Scale(dialog, orient=HORIZONTAL, from_=3, to=9, tickinterval=1, resolution=1)
    btn_go = Button(dialog, text="Начать")
    label.pack(side=TOP)
    hardlist.pack(side=TOP)
    btn_go.pack(side=RIGHT)
    btn_go.bind("<Button-1>", return_and_die)


r = []
word_secret_list = []
word_secret = ""
hard_level = 0
flag = 0
steps = 0
start_new_game()


def num_random(level):
    for i in range(1, 10):
        r.append(i)

    random.shuffle(r)
    temp = random.sample(r, level)
    global word_secret
    for i in temp:
        word_secret += str(i)

    global word_secret_list
    # word_secret_list = word_secret

    return word_secret


def sdaus_new_game():
    global hard_level
    global word_secret
    global word_secret_list
    global flag
    global steps
    global r
    if hard_level != 0:
        mainbox.insert(tkinter.END, '\n       ВЫ СДАЛИСЬ!!!  \n')
        mainbox.insert(tkinter.END, '\nБыло загадано число: ' + str(word_secret) + '\n')
        mainbox.configure(fg="red")
    flag = 0
    word_secret_list = []
    r = []
    hard_level = 0
    word_secret = ""
    steps = 0


def podskaska():
    def dest():
        dialog.destroy()
    if word_secret_list:
        dialog = Tk()
        dialog.title("Подсказка")
        dialog.geometry('200x70+200+100')
        label = Label(dialog, text=u"В этом числе есть цифра " + word_secret_list.pop(), width='100')
        btn_go = Button(dialog, text="ОК")
        label.pack(side=TOP)
        btn_go.pack(side=RIGHT)
        btn_go.bind("<Button-1>", dest)


def start():
    global hard_level
    global word_secret
    global word_secret_list
    global flag
    global steps
    global r
    cows, bulls = cow_bull(enterfill.get())
    word = enterfill.get()
    if (len(word) == hard_level) and (flag == 0) and (hard_level != 0):
        mainbox.insert(tkinter.END, str(word) + '  :  Быки= ' + str(len(bulls)) + '   Коровы=' + str(len(cows)) + '\n')
        steps += 1
        if len(bulls) == hard_level:
            mainbox.insert(tkinter.END, '\n       ВЫ ВЫИГРАЛИ!!!  \n')
            mainbox.insert(tkinter.END, 'Сделано ' + str(steps) + ' шагов.' + '\n')
            mainbox.configure(fg="red")
            flag = 0
            word_secret_list = []
            r = []
            hard_level = 0
            word_secret = ""
            steps = 0
    enterfill.delete(0, END)
    mainbox.see(END)


def cow_bull(word_enter):
    # Количество быков и коров в введённом слове
    # word_enter введённое слово
    # word_secret загаданное слово
    cows = []  # Это "буквы-коровы"
    bulls = []  # Это "буквы-быки"
    for i in range(len(word_enter)):  # перебор по всем буквам введенного
        if word_enter[i] in word_secret:  # если буква есть в загаданном
            if word_enter[i] == word_secret[i]:  # и стоит на своем месте
                bulls.append(word_enter[i])  # она бык
            else:  # если не на своем месте
                cows.append(word_enter[i])  # корова
    return cows, bulls


def info():  # окошко "о программе"
    inform = Tk()

    inform.title("Информация")
    inform.iconbitmap("DATA\\img\\info.ico")

    infoblank = Canvas(inform, width=370, height=200, bg="grey")
    infoblank.create_text(text="В начале игры вы выбираете количество цифр в загадывающемся компьютером числе.\
     Игрок делает первую попытку отгадать число. Попытка — это число с выбранным количеством неповторяющихся цифр, \
     сообщаемое компьютеру. Он сообщает в ответ, сколько цифр угадано без совпадения с их позициями в \
     тайном числе (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество \
     быков). Например: \
     Компьютер задумал число «8234».\
     Попытка: «8743».\
     Вывод: один «бык» (одна цифра «8» угадана вплоть до позиции) и две «коровы» (две цифры: «3» и «4» — угаданы на \
     неверных позициях).")

    infoblank.pack()


root = tkinter.Tk()  # Вот
root.title("Быки и коровы")
root.iconbitmap("DATA\\img\\Bull.ico")

main_menu = Menu(root)  # меню
root.config(menu=main_menu)
root_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Меню", menu=root_menu)
root_menu.add_command(label="Новая игра", command=start_new_game)  # Начать новую игру функцией start_new_game
root_menu.add_command(label="О программе", command=info)
root_menu.add_separator()
root_menu.add_command(label="Выход", command=root.destroy)

frame_1 = tkinter.Frame(root, bg='blue')

mainbox = ScrolledText(frame_1, width=40, height=11, font='12',  # Окно вывода
                       fg="black", bg='lightblue')
enterfill = tkinter.Entry(frame_1, width=5, font='12')  # Окно для ввода
btn_submit = tkinter.Button(frame_1, background='yellow', text="Ввод",
                            relief="groove")  # Кнопка

label1 = tkinter.Label(frame_1, text="Введите цифры: ", bg='blue', fg='yellow',
                       font='8')

# ----------------------------------


btn_submit.bind("<Button-1>", start)
enterfill.bind("<Return>", start)


posk = tkinter.Button(frame_1, background='green', text="Подсказка", relief="groove", command=podskaska)
sdaus = tkinter.Button(frame_1, background='green', text="Сдаюсь", relief="groove", command=sdaus_new_game)

frame_1.grid()

mainbox.grid(row=0, rowspan=10, column=0, columnspan=5)  # Окно вывода

label1.grid(row=11, column=0, sticky="w")

enterfill.grid(row=11, column=1, sticky="w", padx=4, pady=4)  # Окно ввода

btn_submit.grid(row=11, column=2, sticky="w", padx=4, pady=2)  # Кнопка ввода


posk.grid(row=11, column=3, sticky="w")  # Кнопка подсказки
sdaus.grid(row=11, column=4, sticky="e")  # Кнопка сдаюсь
root.resizable(False, False)
root.mainloop()
