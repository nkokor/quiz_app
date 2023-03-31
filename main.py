from tkinter import *
import quiz as quiz
from tkinter import filedialog
from datetime import datetime
import sqlite3

all_questions = [
    ("How many continents are there ?", "7", "5", "3", "10", 1),
    ("How many oceans are there ?", "5", "8", "7", "3", 1),
    ('What is the capital city of France?', "Paris", "Nantes", "Besancon", "Reims", 1),
    ("How many states are in the USA ?", "50", "49", "53", "52", 1),
    ("What is Earth's largest continent ?", "Asia", 'Europe', 'Africa', 'South America', 1),
    ("What river runs through Baghdad ?", "Tigris", "Jordan", "Karun", "Euphrates", 1),
    ("What percentage of the River Nile is located in Egypt ?", "22%", "100%", "9%", "83%", 1),
    ("In what country can you visit Machu Picchu ?", "Peru", "Chile", "Bolivia", "Columbia", 1),
    ("What country is the largest country in the world ?", "Russia", "USA", "Turkey", "UK", 1),
    ("What is the capital city of Australia ?", "Canberra", "Sydney", "Perth", "Melbourne", 1),
    ("Which African nation has the most pyramids ?", "Sudan", "Libya", "Egypt", "Algeria", 1),
    ("How many elements are in the periodic table ?", "118", "212", "200", "120", 2),
    ("What is the pH value of acids ?", "<7", ">7", "7", "0", 2),
    ("The hardest form of carbon is ", "Diamond", "Coke", "Graphite", "Charcoal", 2),
    ("The number of electrons present in H+ is ", "0", "1", "2", "3", 2),
    ("What type of charge does a neutron carry ?", "No charge", "Positive", "Negative", "Oscillating", 2),
    ("Which substances control the rates of chemical reactions ?", "Catalysts", "Isotopes", "Cathodes", "Reactants", 2),
    ("Who discovered hydrogen ?", "H. Cavendish", "D. Hodgkin", "W. Crookes", "B. Shaw", 2),
    ("Who created the periodic table ?", "Dmitri Mendeleev", "Marie Curie", "Karl Benz", "James Watt", 2),
    ("What is the lightest element in the periodic table ?", "Hydrogen", "Aluminum", "Zinc", "Oxygen", 2),
    ("Who invented the telephone ?", "A. G. Bell", "A. Hitler", "M. Curie", "N. Tesla", 3),
    ("What year did WW1 start ?", "1914.", "1939.", "1945.", "1918.", 3),
    ("Which of the following inventions was the first to be patented ?", "Rubber band", "Cash register", "Dishwasher", "Chewing gum", 3),
    ("How long did the Hundred Years' War last ?", "116 years", "100 years", "99 years", "86 years", 3),
    ("Which of the following empires had no written language ?", "Incan Empire", "Aztec Empire", "Tang Dynasty", "Roman Empire", 3),
    ("What did ancient Egyptians use as pillows ?", "Stones", "Animal pelts", "Bags of water", "Bundles of wheat", 3),
    ("Who invented Arabic numerals ?", "Indians", "Arabs", "Greeks", "Romans", 3),
    ("What year did WW2 start ?", "1939.", "1914.", "1945.", "1918.", 3),
    ("How many times has the Mona Lisa been stolen ?", "1", "3", "5", "27", 3),
    ("Who discovered America ?", "Christopher Columbus", "Ferdinand Magellan", "Batman", "Britney Spears", 3),
    ("Whats is the name of Lady Gaga's first album ?", "The Fame", "Born This Way", "Joanne", "Artpop", 4),
    ('Which band became famous for their hit song "Zombies" ?', "The Cranberries", "U2", "The Beatles", "Green day", 4),
    ("Who left Destiny's child first ?", "Beyonce", "Kelly Rowland", "LaTavia Roberson", "Michelle Williams", 4),
    ("Who was awarded the very first gold record ?", "Perry Como", "The Beatles", "Elvis Presley", "Nat King Cole", 4),
    ("What is the name of Adele's first single ?", "Chasing Pavements", "Hello", "Someone like you", "Easy on me", 4),
    ("How many different instruments did Prince play on his debut album ?", "27", "5", "13", "40", 4),
    ("Which song is sung by Ariana Grande ?", "Problem", "Love Story", "Marry You", "Hello", 4),
    ("Who created One Direction ?", "Nicole Scherzinger", "Simon Cowell", "Kanye West", "Beyonce", 4),
    ("What's the name of our galaxy ?", "Milky Way", "Snickers", "Mars", "Kinder Bueno", 5),
    ("What is the biggest planet in the Solar System ?", "Jupiter", "Saturn", "Pluto", "Venus", 5),
    ("Who was the first man to land on the moon ?", "Neil Armstrong", "Eugene Cernan", "Bruno Mars", "John Glenn", 5),
    ("What planet is the closest to Earth ?", "Mercury", "Pluto", "Saturn", "Jupiter", 5),
    ("What color is the sunset on Mars ?", "Blue", "Red", "Green", "Orange", 5),
    ("How old is the Universe ?", "13.7 billion years", "137 billion years", "1.37 billion years", "6 000 years", 5),
    ("How many Earths could fit inside the Sun ?", "1 million", "100 thousand", "10 million", "1 thousand", 5),
    ("What color is Saturn ?", "Yellow", "Red", "Purple", "Blue", 5),
    ("What kind of star is our sun ?", "Yellow dwarf", "White dwarf", "Red dwarf", "Red giant", 5)
]

connection = sqlite3.connect('quiz.db')


def check_table_exists(dbcon):
    c = dbcon.cursor()
    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='questions'")
    return c.fetchone()[0] == 1


def has_records(dbcon):
    c = dbcon.cursor()
    c.execute("SELECT count(*) FROM questions")
    return c.fetchone()[0] != 0


if not check_table_exists(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE questions (
                      question_text text,
                      right_answer text,
                      answer_a text,
                      answer_b text,
                      answer_c text,
                      category integer)
    """)
    connection.commit()
    cursor.executemany("INSERT INTO questions VALUES (?,?,?,?,?,?)", all_questions)
    connection.commit()


if check_table_exists(connection) and not has_records(connection):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO questions VALUES (?,?,?,?,?,?)", all_questions)
    connection.commit()

quiz = quiz.Quiz('Train Your Brain')


def on_enter_again(event):
    play_button.config(background='firebrick2', foreground="white")


def on_leave_again(event):
    play_button.config(background='white', foreground='black')


def on_enter_review(event):
    review_button.config(fg='medium turquoise')


def on_leave_review(event):
    review_button.config(fg='grey')


def on_enter_save(event):
    save_label.config(fg='medium turquoise')


def on_enter_leave(event):
    save_label.config(fg='grey')


def on_enter_start(event):
    start_button.config(background='firebrick2', foreground="white")


def on_leave_start(event):
    start_button.config(background='white', foreground='black')


def on_enter(event):
    button_next.config(background='medium turquoise', foreground="white")


def on_leave(event):
    button_next.config(background='white', foreground='black')


def on_enter_a(event):
    answer_a.config(background='Misty Rose3')


def on_leave_a(event):
    answer_a.config(background='white', foreground='black')


def on_enter_b(event):
    answer_b.config(background='Misty Rose3')


def on_leave_b(event):
    answer_b.config(background='white', foreground='black')


def on_enter_c(event):
    answer_c.config(background='Misty Rose3')


def on_leave_c(event):
    answer_c.config(background='white', foreground='black')


def on_enter_d(event):
    answer_d.config(background='Misty Rose3')


def on_leave_d(event):
    answer_d.config(background='white', foreground='black')


def hide_review(event):
    global label1
    global label2
    global label3
    global label4
    global label5
    global review_button
    global save_label

    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    save_label.destroy()

    review_button.config(text='Review', cursor='hand2')
    review_button.bind('<Button-1>', review)


def save_report(event):
    today = datetime.today()
    today = today.strftime("%B %d, %Y %H:%M:%S")
    report = today
    report += '''
'''
    for i in range(1, len(quiz.answers) + 1):
        report += f'''
{i}) {quiz.answers[i-1][0].line}
   Your answer: {quiz.answers[i-1][1]}
   Correct answer: {quiz.answers[i-1][0].right_answer}
'''
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Kokor\\Documents", defaultextension='.txt', filetypes=[("Text file (.txt)", '.txt')])
    if file is None:
        return
    file.write(report)
    file.close()


def review(event):
    global label1
    global label2
    global label3
    global label4
    global label5
    global review_button
    global f
    global save_label

    review_button.config(text='Hide')
    review_button.bind('<Button-1>', hide_review)

    label1 = Label(f, text=f'''1) {quiz.answers[0][0].line}: {quiz.answers[0][0].get_emoji(quiz.answers[0][1])}     Your answer: {quiz.answers[0][1]}    |    Correct answer: {quiz.answers[0][0].right_answer}''', bg='white', font=('Microsoft YaHei Light', 9), anchor=W)
    label1.grid(row=0, sticky=W)
    label2 = Label(f, text=f'''2) {quiz.answers[1][0].line}: {quiz.answers[1][0].get_emoji(quiz.answers[1][1])}     Your answer: {quiz.answers[1][1]}    |    Correct answer: {quiz.answers[1][0].right_answer}''', bg='white', font=('Microsoft YaHei Light', 9), anchor=W)
    label2.grid(row=1, sticky=W)
    label3 = Label(f, text=f'''3) {quiz.answers[2][0].line}: {quiz.answers[2][0].get_emoji(quiz.answers[2][1])}     Your answer: {quiz.answers[2][1]}    |    Correct answer: {quiz.answers[2][0].right_answer}''', bg='white', font=('Microsoft YaHei Light', 9), anchor=W)
    label3.grid(row=2, sticky=W)
    label4 = Label(f, text=f'''4) {quiz.answers[3][0].line}: {quiz.answers[3][0].get_emoji(quiz.answers[3][1])}     Your answer: {quiz.answers[3][1]}    |    Correct answer: {quiz.answers[3][0].right_answer}''', bg='white', font=('Microsoft YaHei Light', 9), anchor=W)
    label4.grid(row=3, sticky=W)
    label5 = Label(f, text=f'''5) {quiz.answers[4][0].line}: {quiz.answers[4][0].get_emoji(quiz.answers[4][1])}     Your answer: {quiz.answers[4][1]}    |    Correct answer: {quiz.answers[4][0].right_answer}''', bg='white', font=('Microsoft YaHei Light', 9), anchor=W)
    label5.grid(row=4, sticky=W)

    save_label = Label(f, text='''
       Save report''', bg='white', fg='grey', anchor=E, cursor='hand2')
    save_label.grid(row=5, column=1, sticky=E, padx=7)
    save_label.bind('<Enter>', on_enter_save)
    save_label.bind('<Leave>', on_enter_leave)
    save_label.bind('<Button-1>', save_report)


def finish():
    global brain_label2
    global question_base
    global result_label
    global pass_image
    global brain_label
    global status
    global question_frame
    global play_button
    global review_button
    global lbl
    global message
    global f
    global finish_frame

    finish_frame = Frame(root, bg='white')
    finish_frame.pack(pady=60)

    if choice.get() != 0:
        quiz.add_answer(quiz.used_questions[4], quiz.used_questions[4].answers[choice.get() - 1])
    else:
        quiz.add_answer(quiz.used_questions[4], 'Not answered')

    brain_label2.destroy()
    question_base.destroy()
    brain_label.destroy()
    status.destroy()

    rez = quiz.correct

    if rez < 3:
        pass_image = PhotoImage(file='images/fail.png')
        message = Label(finish_frame, text='''Seems like you need to work a bit harder...
    Remember to not give up !''', bg='white', font=('Kristen ITC', 20))

    if rez >= 3:
        pass_image = PhotoImage(file='images/success.png')
        message = Label(finish_frame, text='''Congrats !
    You have a strong, healthy brain !''', bg='white', font=('Kristen ITC', 20))

    lbl = Label(finish_frame, image=pass_image, bg='white')
    lbl.pack(pady=10)

    result_label = Label(finish_frame, text=f'''{rez}/5''', font=('Microsoft YaHei', 13), bg='white')
    result_label.pack()

    message.pack(anchor=CENTER)

    review_button = Label(finish_frame, text='Review', bg='white', fg='grey', cursor='hand2')
    review_button.pack(pady=14)
    review_button.bind('<Button-1>', review)
    review_button.bind('<Enter>', on_enter_review)
    review_button.bind('<Leave>', on_leave_review)

    f = Frame(finish_frame, bg='white', width=800, height=131)
    f.pack(pady=9)

    play_button = Button(root, text='Play again', command=lambda: play_quiz(0), font=('Microsoft YaHei Light', 14),
                         bg='white', activebackground='firebrick2', activeforeground='black', cursor='hand2')
    play_button.place(x=711, y=700)
    play_button.bind('<Enter>', on_enter_again)
    play_button.bind('<Leave>', on_leave_again)


root = Tk()
root.minsize(1000, 580)
root.state('zoomed')
root.config(bg='white')
root.title('Train Your Brain')
root.iconbitmap('images/icon.ico')
first_game = True


def show_bubble(event):
    global bubble_lbl
    bubble_lbl = Label(root, image=bubble_image, bg='white')
    bubble_lbl.place(x=450, y=445)


def hide_bubble(event):
    global bubble_lbl
    bubble_lbl.destroy()


def play_quiz(question_number):
    global good_luck_label
    global luck_label
    global greet_frame
    global finish_frame
    global question_base
    global f
    global play_button
    global brain_label
    global question_label
    global button_next
    global answer_a
    global answer_b
    global answer_c
    global answer_d
    global status
    global question_frame
    global start_button
    global review_button
    global label1
    global label2
    global label3
    global label4
    global label5
    global result_label
    global message
    global lbl
    global brain_label2

    greet_frame.destroy()
    luck_label.destroy()
    good_luck_label.destroy()
    question_base.destroy()
    f.destroy()
    result_label.destroy()
    message.destroy()
    lbl.destroy()
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    play_button.destroy()
    start_button.destroy()
    brain_label.destroy()
    brain_label2.destroy()
    question_label.destroy()
    answer_a.destroy()
    answer_b.destroy()
    answer_c.destroy()
    answer_d.destroy()
    question_frame.destroy()
    button_next.destroy()
    status.destroy()
    review_button.destroy()
    finish_frame.destroy()

    if question_number == 0:
        quiz.generate_new_quiz()

    if question_number != 0:
        if choice.get() != 0:
            quiz.add_answer(quiz.used_questions[question_number - 1],
                            quiz.used_questions[question_number - 1].answers[choice.get() - 1])
        else:
            quiz.add_answer(quiz.used_questions[question_number - 1], 'Not answered')

    question_base = Frame(root, bg='white', pady=120)
    question_base.pack()

    question_frame = LabelFrame(question_base, text='Question ' + str(question_number + 1), padx=150, pady=40, bg='white', width=800, font=('Microsoft YaHei', 10), fg='firebrick2')
    question_frame.grid(row=0, column=0)

    question_label = Label(question_frame, text=f'''{quiz.used_questions[question_number].line}

        ''', bg='white', font=("Kristen ITC", 12), anchor=CENTER, width=50)
    question_label.grid(row=0, column=0, columnspan=4)

    choice.set(0)

    answer_a = Radiobutton(question_frame, text='A:  ' + quiz.used_questions[question_number].answers[0], bg='white',
                           variable=choice, value=1, indicatoron=False, width=20, anchor=W, font=('Microsoft YaHei', 10),
                           cursor='hand2')
    answer_b = Radiobutton(question_frame, text='B:  ' + quiz.used_questions[question_number].answers[1], bg='white',
                           variable=choice, value=2, indicatoron=False, width=20, anchor=W, font=('Microsoft YaHei', 10),
                           cursor='hand2')
    answer_c = Radiobutton(question_frame, text='C:  ' + quiz.used_questions[question_number].answers[2], bg='white',
                           variable=choice, value=3, indicatoron=False, width=20, anchor=W, font=('Microsoft YaHei', 10),
                           cursor='hand2')
    answer_d = Radiobutton(question_frame, text='D:  ' + quiz.used_questions[question_number].answers[3], bg='white',
                           variable=choice, value=4, indicatoron=False, width=20, anchor=W, font=('Microsoft YaHei', 10),
                           cursor='hand2')
    answer_a.grid(row=1, column=1, sticky=E)
    answer_b.grid(row=1, column=2, sticky=W)
    answer_c.grid(row=2, column=1, sticky=E)
    answer_d.grid(row=2, column=2, sticky=W)

    answer_a.bind('<Enter>', on_enter_a)
    answer_a.bind('<Leave>', on_leave_a)
    answer_b.bind('<Enter>', on_enter_b)
    answer_b.bind('<Leave>', on_leave_b)
    answer_c.bind('<Enter>', on_enter_c)
    answer_c.bind('<Leave>', on_leave_c)
    answer_d.bind('<Enter>', on_enter_d)
    answer_d.bind('<Leave>', on_leave_d)

    brain_label = Label(root, image=image, bg='white')
    brain_label.place(x=0, y=480)

    brain_label2 = Label(root, image=brain_image_read, bg='white')
    brain_label2.place(x=260, y=590)
    brain_label2.bind('<Enter>', show_bubble)
    brain_label2.bind('<Leave>', hide_bubble)

    if question_number == 4:
        button_next = Button(question_base, text='Finish', command=finish, width=10, height=1, bg='white',
                             activebackground='medium turquoise', font=('Microsoft YaHei Light', 12), cursor='hand2')

    else:
        button_next = Button(question_base, text='Next', command=lambda: play_quiz(question_number + 1), width=10,
                             height=1, bg='white', activebackground='medium turquoise', font=('Microsoft YaHei Light', 12),
                             cursor='hand2')
    button_next.grid(row=1, column=0, sticky=E, pady=30)
    button_next.bind('<Enter>', on_enter)
    button_next.bind('<Leave>', on_leave)

    status = Label(root, text='Question ' + str(question_number + 1) + ' of ' + str(len(quiz.used_questions)),
                   relief=SUNKEN, bd=1, anchor=W, bg='white')
    status.pack(side=BOTTOM, fill=X)

rules = [
    ('There are 5 questions in this quiz.'),
    ('It takes 3 correct answers to pass the quiz.'),
    ('Once you move onto the next question, you cannot go back.')
]

greet_frame = Frame(root, bg='white')
greet_frame.pack(pady=50)
hello = Label(greet_frame, text='Hello!', font=('Kristen ITC', 19), bg='white')
hello.pack()
welcome = Label(greet_frame, text=f'''Welcome to ''', font=('Kristen ITC', 19), bg='white')
welcome.pack()
title = Label(greet_frame, text=quiz.title, font=('Kristen ITC', 63), bg='white', fg='firebrick2')
title.pack(pady=10)
rule = Label(greet_frame, text='The rules are simple!', font=('Microsoft YaHei', 14), bg='white')
rule.pack(pady=10)

for r in rules:
    new_rule = Label(greet_frame, text=r, bg='white', fg='Misty Rose3', font=('Microsoft YaHei', 12))
    new_rule.pack()

good_luck_image = PhotoImage(file='images/welcome_image.png')
good_luck_label = Label(root, bg='white', image=good_luck_image)
good_luck_label.place(x=10, y=630)
luck_image = PhotoImage(file='images/luck.png')
luck_label = Label(root, bg='white', image=luck_image)
luck_label.place(x=220, y=500)

hit = Label(greet_frame, text='''








Hit the button whenever you're ready!''', bg='white', font=('Microsoft YaHei', 14))
hit.pack()


start_button = Button(root, text='Start quiz', font=('Microsoft YaHei Light', 14), activebackground='firebrick2',
                      bg='white', cursor='hand2',
                      width=10, command=lambda: play_quiz(0))

start_button.bind('<Enter>', on_enter_start)
start_button.bind('<Leave>', on_leave_start)
start_button.place(x=713, y=700)

choice = IntVar()
choice.set(0)

bubble_image = PhotoImage(file='images/bubble.png')
brain_image_read = PhotoImage(file='images/new.png')
image = PhotoImage(file="images/books.png")

image_label = Label(root)
play_button = Button(root)
brain_label = Label(root)
button_next = Button(root)
status = Label(root)
review_button = Label(root)
label1 = Label(root)
label2 = Label(root)
label3 = Label(root)
label4 = Label(root)
label5 = Label(root)
lbl = Label(root)
pass_image = PhotoImage
result_label = Label(root)
message = Label(root)
f = Frame(root)
save_label = Label(f)
question_base = Frame(root)
question_frame = LabelFrame(question_base)
question_label = Label(question_frame)
answer_a = Radiobutton(question_frame)
answer_b = Radiobutton(question_frame)
answer_c = Radiobutton(question_frame)
answer_d = Radiobutton(question_frame)
finish_frame = Frame(root)
bubble_lbl = Label(root)
brain_label2 = Label(root)

mainloop()
