from tkinter import*
import turtle
import random
from tkinter import messagebox
from tkinter import ttk
window = Tk()
window.title("Hangman")
window.geometry("1000x700")
window.config(bg="mistyrose")

tries = 6
score = 0
def how():
    global inst, rule_, back
    title.destroy()
    play.destroy()
    text_box.destroy()
    how_to.destroy()
    nlabel.destroy()
    window.config(bg="lightgrey")
    inst = Label(window, text="INSTRUTIONS", font=("Arial", 20), bg="lightgrey")
    inst.pack(side=TOP, fill=X)
    rule = """\n\n1. When the button 'Play' is clicked, dashed lines appears, representing the length of the word to be 
    guessed.
\n2. Above the dashed lines, the category of the object[word] will be given, which is to be 
guessed.
\n3. A player gets 6 tries, which is deducted when a wrong guessed[letter button] is 
attempted.
\n4. A player must guess the word before a man is drawn by the circle being 
hanged.
\n5. If an incorrect answer is made, the total score is reset.
\n6. Make sure the turtle completes its figure before clicking another button to avoid mis-drawings.
\n\n"""
    rule_ = Label(window, text=rule, font=('Comic Sans MS', 15), justify="left")
    rule_.pack(fill=X)
    back = ttk.Button(window, text="Back",command=backhow)
    back.place(x = 430, y=550)

def backhow():
    inst.destroy()
    rule_.destroy()
    back.destroy()
    window.config(bg="mistyrose")
    main()
selection = ''
def playtab():
    global tries, score, tries_, score_, label, screen, lframe, uframe, nlabel
    title.destroy()
    text_box.destroy()
    play.destroy()
    how_to.destroy()
    window.config(bg="floralwhite")
    title.destroy()
    play.destroy()
    how_to.destroy()
    nlabel.destroy()
    label = Label(window, text="Guess the word before the man hangs!", font=('Arial', 15, "bold", "underline"), bg="floralwhite", fg="Red")
    label.pack(side=TOP, fill = X)
    uframe = Frame(master=window, border=5, relief=SUNKEN )
    uframe.place(x = 180, y = 30, height=300, width=600)
    screen = turtle.ScrolledCanvas(uframe)
    screen.pack()
    my_turtle = turtle.RawTurtle(screen, shape='circle')
    my_turtle.speed(6)
    words = {"Food and Sweets" : ['CAKE', 'CRISPS', 'CHOCOLATE', 'FRENCHFRIES', 'PIZZA', 'PAELLA', 'CROISSANT', 'BIRYANI', 'CEVICHE', 'FAJITAS', 'RISOTTO', 'POHA', 'PHO', 'RAMEN', 'RASGULLA', 'JALEBI', "CHOCOLAVA", "SAMOSA", "BHELPURI", "MISALPAV", "FRANKIE", "APFELSTRUDEL"], 
             "Beverages" : ['LATTE', 'FRUITPUNCH', 'ICETEA', 'LIMESODA', 'LASSI', 'YAKULT', 'FANTA', 'COKE', 'MOJITO', 'CHAMPAGNE', 'TEQUILA', "JIGARTHANDA", "SHIKANJVI", "PANAKAM", "JALJEERA", "BURANSH", "WATER", "MIRINDA"], 
             "Game" : ['BADMINTON', 'BASKETBALL', 'TENNIS', 'MINECRAFT', 'FOOTBALL', 'CRICKET', 'HOCKEY', 'CHESS', 'POLO', 'PACKMAN', 'GTA', 'UNO','SUDOKU', 'DODGEBALL', 'VOLLEYBALL', 'BASEBALL', 'HOPSCOTCH', "CYCLING", "BOBSLEIGH", "FENCING", ], 
             'Verb' : ['COOKING', 'DANCE', 'STUDYING', 'SWIMMING', 'SING', 'PAINTING', 'COLORING', 'SLEEPING', 'SCULPTURE', 'THINK', 'CODING', 'PLAYING'], 
             "Music" : ["POPMUSIC", "ROCK", "JAZZ", "REGGAE", "DISCO", "SYNTHPOP", "PUNKPOP", "BLUES", "SKA", "GOSPEL", "EDM"], 
             "Country" : ["ANDORRA", "AZERBAIJAN", "MADAGASCAR", "MOLDOVA", "BELGIUM", "BOLIVIA", "BOSNIA", "HERZEGOVINA", "BAHAMAS", "AFGHANISTAN", "AUSTRALIA", "AUSTRIA", "ARMENIA", "ALGERIA", "BANGLADESH", "BRAZIL", "BURUNDI", "CAMBODIA", "CANADA", "CHILE", "CHINA", "COLOMBIA", "COMOROS", "CONGO", "CZECHOSOLVAKIA", 'DENMARK', 'DOMINICA', 'ECUADOR', 'ESTONIA', 'ETHIOPIA', 'ESWATINI', 'EGYPT', 'FIJI', 'FINLAND', 'FRANCE', 'GEORGIA', 'GERMANY', 'GREECE', 'GRENADA', "GUATEMALA", 'GUINEA', 'GUYANA', "HAITI", 'HUNGARY', 'HONDURAS', 'INDIA', 'ICELAND', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JORDAN', 'JAPAN', 'KENYA', 'KOSOVO', 'KUWAIT', 'KOREA', 'KIRIBATI', 'KURGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA', 'LITHUANIA', 'LUXEMBORG', 'ZAMBIA', 'ZIMBABWE', 'YEMEN', 'WUTTEMBERG', 'VIETNAM', 'VENEZUELA', 'UZBEKISTAN', 'URUGUAY', 'UKRAINE', 'UGANDA', 'TOGO', 'TURKEY', 'TUNISIA', 'TUVALU', 'TONGA', 'THAILAND', 'SYRIA', 'SURINAME', 'SUDAN', 'SLOVENIA', 'SLOVAKIA', 'SEYCHELLES', 'SENEGAL', 'SAMOA' 'RWANDA', 'QATAR', 'PARAGUAY', 'OMAN', 'NORWAY', 'NICARAGUA', 'NAURU', 'MOZAMBIQUE', 'MONTENEGRO', 'MALAWI']
             ,"Colour" : ["CHARTREUSE", 'LAVENDAR', 'TURQUOISE', 'CRIMSON', 'AZURE', 'ORCHID', 'AMBER', 'AMETHYST', 'APRICOT', 'AQUAMARINE', 'BEAVER', 'BEIGE', 'BISQUE', 'BURLYWOOD', 'BYZANTIUM', 'CATAWBA', 'CELESTE', 'CELADON', 'CERULEAN', 'CHESTNUT', 'CINEREOUS', 'EMINENCE', 'FANDANGO', 'FROSTBITE', 'FULVOUS', 'BLUE', 'GREEN', 'MUSTARD'], 
             "Professions" : ["ARCHITECT",'PHARMACIST', 'VETERINARIAN', 'JAURNALIST', 'ELECTRICIAN', 'ACUPUNCTURIST', 'ATTORNEY', 'BARTENDER', 'BUSINESSMAN', 'COACH', 'DENTIST', 'DIETICIAN', 'ECONOMIST', 'ENGINEER', 'ELECTRICIAN','ASTRONOMER', 'FIREMAN', 'FLORIST', 'ADVOCATE', 'LAWYER', 'OPTICIAN', 'PHOTOGRAPHER', 'SOLDIER', 'SURGEON' ]
             }
    category = ['Food and Sweets', 'Beverages', 'Game', 'Verb', 'Music', 'Country', 'Colour', 'Professions']
    tries = 6
    tries_ = Label(window, text= "Tries : " +str(tries), bg="floralwhite", font=('Arial', 15))
    tries_.place(y=340, x=420)
    score_ = Label(window, text="Score : "+str(score), bg='floralwhite', font=('Arial', 15))
    score_.place(x=420, y=365)
    mlabel= Label(window, text="By Nitya Gargi Srivastava\nClass : XII B2\nGaurs Internal School",bg='floralwhite')
    mlabel.place(x=800, y=70)

    def base():
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(200)
        my_turtle.right(180)
        my_turtle.pendown()
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.left(90)
        my_turtle.forward(400)
        my_turtle.right(180)
        my_turtle.forward(400)
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.right(90)
        my_turtle.forward(400)
        my_turtle.left(180)
        my_turtle.forward(200)
        my_turtle.left(90)
        my_turtle.forward(30)
        my_turtle.right(90)
        global gcategory_, gword_, gword, gcategory
        gcategory = random.choice(category)
        gword = random.choice(words[gcategory])
        gcategory_ = Label(window, text= gcategory, bg="floralwhite", font = ('Arial', 15))
        gcategory_.place(y=400, x=425)
        gword_ = Label(window, text="-"*len(gword), bg='floralwhite', font=('Arial', 30))
        gword_.place(y=425, x = 425)
    base()
    def restart():
        global gword_, gcategory_, tries
        for button in buttons.values():
            button.config(bg="skyblue")
        tries = 6
        tries_.config(text="Tries : " + str(tries))
        buttons[selection].config(bg="skyblue")
        my_turtle.clear()
        my_turtle.reset()
        my_turtle.speed(5)
        gword_.config(text='')
        gcategory_.config(text='')
        base()
    lframe = Frame(master=window, border=5, relief=SUNKEN, bg="rosybrown")
    lframe.place(x=50, y = 480, height=200, width=880)
    def assign_value(value):
        global selection, tries, score
        selection = value
        current_word = gword_.cget("text")
        if selection in gword:
            new_word = ""
            for i, letter in enumerate(gword):
                if letter == selection:
                    new_word += selection
                else:
                    if i < len(current_word) and current_word[i] != '-':
                        new_word += current_word[i]
                    else:
                        new_word += '-'
            gword_.config(text=new_word)
        else:
            tries -=1
            tries_.config(text="Tries: " + str(tries))
            buttons[selection].config(bg="crimson")
            if tries ==5:
                my_turtle.circle(20)
                my_turtle.circle(20, 180)
                my_turtle.right(90)
            if tries ==4:
                my_turtle.forward(70)
                my_turtle.backward(70)
            if tries==3:
                my_turtle.right(45)
                my_turtle.forward(40)
                my_turtle.backward(40)
                my_turtle.left(45)
            if tries==2:
                my_turtle.left(45)
                my_turtle.forward(40)
                my_turtle.backward(40)
                my_turtle.right(45)
                my_turtle.forward(70)
            if tries==1:
                my_turtle.right(45)
                my_turtle.forward(40)
                my_turtle.backward(40)
                my_turtle.left(45)
            if tries==0:
                my_turtle.left(45)
                my_turtle.forward(40)
                my_turtle.backward(40)
                my_turtle.right(45)
                messagebox.showerror("Word not Guessed!", f"The word was {gword}")
                score=0
                score_.config(text="Score : " +str(score))
                restart()
        try:
            if new_word==gword:
                messagebox.showinfo("Word guessed!", "Congratulation!!")
                score +=1
                score_.config(text="Score : "+str(score))
                restart()
        except:
            pass
    ba = Button(lframe, text="A", font=("MS Comic Sans", 14), bg="skyblue", width=7, command = lambda: assign_value("A"))
    ba.grid(row=2, column=2, pady=5)
    bb =Button(lframe, text="B", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('B'))
    bb.grid(row=4, column=8, pady=5)
    bc = Button(lframe, text="C", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('C'))
    bc.grid(row=4, column=4, pady=5)
    bd = Button(lframe, text="D", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('D'))
    bd.grid(row=2, column=6, pady=5)
    be  = Button(lframe, text ="E", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('E'))
    be.grid(row=0, column=4, pady=5)
    bf = Button(lframe, text="F", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('F'))
    bf.grid(row=2, column=8, pady=5) 
    bg = Button(lframe, text="G", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('G'))
    bg.grid(row=2, column=10, pady=5)
    bh = Button(lframe, text="H", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('H'))
    bh.grid(row=2, column=12, pady=5)
    bi = Button(lframe, text="I", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('I'))
    bi.grid(row=0, column=14, pady=5)
    bj = Button(lframe, text="J", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('J'))
    bj.grid(row=2, column=14, pady=5) 
    bk = Button(lframe, text="K", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('K'))
    bk.grid(row=2, column=16, pady=5) 
    bl = Button(lframe, text="L", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('L'))
    bl.grid(row=2, column=18, pady=5)
    bm =Button(lframe, text="M", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('M'))
    bm.grid(row=4, column=12, pady=5)
    bn =Button(lframe, text="N", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('N'))
    bn.grid(row=4, column=10, pady=5)
    bo = Button(lframe, text="O", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('O'))
    bo.grid(row=0, column=16, pady=5)
    bp = Button(lframe, text="P", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('P'))
    bp.grid(row=0, column=18, pady=5)
    bq  = Button(lframe, text="Q", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('Q'))
    bq.grid(row=0, column=0, pady=5)
    br = Button(lframe, text="R", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('R'))
    br.grid(row=0, column=6, pady=5) 
    bs = Button(lframe, text="S", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('S'))
    bs.grid(row=2, column=4, pady=5)
    bt = Button(lframe, text="T", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('T'))
    bt.grid(row = 0, column=8, pady=5)
    bu = Button(lframe, text="U", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('U'))
    bu.grid(row=0, column=12, pady=5)
    bv =Button(lframe, text="V", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('V'))
    bv.grid(row=4, column=6, pady=5)
    bw = Button(lframe, text="W",font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('W'))
    bw.grid(row=0, column=2, pady=5)
    bx= Button(lframe, text="X", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('X'))
    bx.grid(row=4, column=2, pady=5) 
    by = Button(lframe, text="Y", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('Y'))
    by.grid(row=0, column=10, pady=5)
    bz = Button(lframe, text="Z", font=("MS Comic Sans", 14), bg="skyblue", width=7,command = lambda: assign_value('Z'))
    bz.grid(row= 4, column=0, pady=5)
    buttons = {'A' : ba, 'B' :bb , 'C' :bc, 'D':bd, 'E':be, 'F':bf, 'G':bg, 'H':bh, 'I':bi, 'J':bj, 'K':bk, 'L':bl, 'M':bm, 'N':bn, 'O':bo, 'P':bp, 'Q':bq, 'R':br, 'S':bs, 'T':bt, 'U':bu, 'V':bv, 'W':bw, 'X':bx, 'Y':by, 'Z':bz}

def main():
    global title, play, how_to, text_box, nlabel
    shape = """
         |¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯
         |                       ◯
         |                      /|\\
         |                      / 
         |__________________________
                             
                             HANGM_?_N"""
    title = Label(window, text="Hangman", font=('Comic Sans MS', 35, 'bold'),bg='mistyrose')
    title.place(x=400, y=100)
    play = Button(window, text="Play",font=("Comic ", 14), width=7, command=playtab)
    play.place(x = 450, y=440)
    how_to = Button(window, text="How To Play", font=("Comic Sans MS", 14), width=10, command=how)
    how_to.place(x = 430, y=500)
    text_box = Text(window,height=10,width=40)
    text_box.config(font=('Comic Sans MS', 10))
    text_box.place(x = 350, y = 200)
    text_box.delete('1.0', 'end')  
    text_box.insert('end', shape)
    text_box.tag_configure("center", justify='center')
    nlabel= Label(window, text="By Nitya Gargi Srivastava\nClass : XII B2\nGaurs Internal School",bg='mistyrose')
    nlabel.place(x=800, y=600)
main()
window.mainloop()