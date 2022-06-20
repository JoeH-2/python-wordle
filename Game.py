from tkinter import *
import keyboard
import random

MainWindow = Tk()
MainWindow.title("Wordle")
MainWindow.geometry("630x950")
MainWindow.configure(bg='black')

def validate(P):
    if len(P) == 0:
        # empty Entry is ok
        return True
    elif len(P) == 1:
        # Entry with 1 chr is ok
        keyboard.send("tab")
        return True
    else:
        # Anything else, reject it
        return False
vcmd = (MainWindow.register(validate), '%P')

words = []
doc = open("words.txt", "r")
for line in doc:
    x=line.lower()
    words.append(x[:5])

yval = 120

streak = 0
V1 = StringVar()
V2 = StringVar()
V3 = StringVar()
V4 = StringVar()
V5 = StringVar()

def Check():
    global guess
    if answer != guess:
        global yval
        guess = []
        guess.append(V1.get().upper())
        guess.append(V2.get().upper())
        guess.append(V3.get().upper())
        guess.append(V4.get().upper())
        guess.append(V5.get().upper())
        #Check guess to word, let by let
        for let in range (0,len(word)):
            grey = True
            num = 0
            for x in range (0,len(word)):
                if guess[let] == word[x]:
                    num +=1
            for x in range (0,len(word)):
                if guess[let] == word[x]:
                    grey = False
                    if let == 0:
                        global L1
                        L1.destroy()
                        if x == 0:
                            T1 = Label(MainWindow, bg="green", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T1.place(x=20,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="green", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=85,y=yval)
                            break
                        else:
                            T1 = Label(MainWindow, bg="orange", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T1.place(x=20,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="orange", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=85,y=yval)
                    if let == 1:
                        global L2
                        L2.destroy()
                        if x == 1:
                            T2 = Label(MainWindow, bg="green", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T2.place(x=140,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="green", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=205,y=yval)
                            break
                        else:
                            T2 = Label(MainWindow, bg="orange", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T2.place(x=140,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="orange", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=205,y=yval)
                    if let == 2:
                        global L3
                        L3.destroy()
                        if x == 2:
                            T3 = Label(MainWindow, bg="green", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T3.place(x=260,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="green", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=325,y=yval)
                            break
                        else:
                            T3 = Label(MainWindow, bg="orange", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T3.place(x=260,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="orange", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=325,y=yval)
                    if let == 3:
                        global L4
                        L4.destroy()
                        if x == 3:
                            T4 = Label(MainWindow, bg="green", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T4.place(x=380,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="green", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=445,y=yval)
                            break
                        else:
                            T4 = Label(MainWindow, bg="orange", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T4.place(x=380,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="orange", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=445,y=yval)
                    if let == 4:
                        global L5
                        L5.destroy()
                        if x == 4:
                            T5 = Label(MainWindow, bg="green", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T5.place(x=500,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="green", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=565,y=yval)
                            break
                        else:
                            T5 = Label(MainWindow, bg="orange", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T5.place(x=500,y=yval)
                            if num > 1:
                                xx = Label(MainWindow, bg="orange", font=("Calibri 18"), width=3, text = ("x"+str(num)))
                                xx.place(x=565,y=yval)
                else:
                    if grey == True:
                        if let == 0:
                            L1.destroy()
                            T1 = Label(MainWindow, bg="grey18", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T1.place(x=20,y=yval)
                        if let == 1:
                            L2.destroy()
                            T2 = Label(MainWindow, bg="grey18", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T2.place(x=140,y=yval)
                        if let == 2:
                            L3.destroy()
                            T3 = Label(MainWindow, bg="grey18", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T3.place(x=260,y=yval)
                        if let == 3:
                            L4.destroy()
                            T4 = Label(MainWindow, bg="grey18", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T4.place(x=380,y=yval)
                        if let == 4:
                            L5.destroy()
                            T5 = Label(MainWindow, bg="grey18", font=("Calibri 50"), width=3, text = guess[let], fg = "white", bd = "4")
                            T5.place(x=500,y=yval)
        yval = yval + 120
        V1.set('')
        V2.set('')
        V3.set('')
        V4.set('')
        V5.set('')
        if answer != guess:
            global lives
            lives -= 1
            if lives == 0:
                Lose = Label(MainWindow, bg="grey18", font=("Calibri 45"), width=19, text = "0 attempts left :(", fg = "white")
                Lose.place(x=19,y=yval)
                Retry = Button(MainWindow, text="Again?", font=("Calibri 29"), width=29, command=Restart)
                Retry.place(x=23,y=17)
                global streak
                streak = 0
            else:
                create()
        else:
            streak +=1
            title = ("Congratulations! Streak x"+str(streak))
            Congrats = Label(MainWindow, bg="grey18", font=("Calibri 34"), width=25, text=title, fg = "white")
            Congrats.place(x=24,y=yval)
            Retry = Button(MainWindow, text="Again?", font=("Calibri 29"), width=29, command=Restart)
            Retry.place(x=23,y=17)

#GUI
def create():
    global L1
    L1 = Entry(MainWindow, font=("Calibri 50"), width=3, validate="key", validatecommand=vcmd, justify='center', textvariable = V1, bg = "black", fg = "white", bd = "4")
    L1.place(x=20,y=yval)
    L1.insert(0, "")

    global L2
    L2 = Entry(MainWindow, font=("Calibri 50"), width=3, validate="key", validatecommand=vcmd, justify='center', textvariable = V2, bg = "black", fg = "white", bd = "4")
    L2.place(x=140,y=yval)
    L2.insert(0, "")

    global L3
    L3 = Entry(MainWindow, font=("Calibri 50"), width=3, validate="key", validatecommand=vcmd, justify='center', textvariable = V3, bg = "black", fg = "white", bd = "4")
    L3.place(x=260,y=yval)
    L3.insert(0, "")

    global L4
    L4 = Entry(MainWindow, font=("Calibri 50"), width=3, validate="key", validatecommand=vcmd, justify='center', textvariable = V4, bg = "black", fg = "white", bd = "4")
    L4.place(x=380,y=yval)
    L4.insert(0, "")

    global L5
    L5 = Entry(MainWindow, font=("Calibri 50"), width=3, validate="key", validatecommand=vcmd, justify='center', textvariable = V5, bg = "black", fg = "white", bd = "4")
    L5.place(x=500,y=yval)
    L5.insert(0, "")

    CheckButton = Button(MainWindow, text="Guess", font=("Calibri 29"), width=29, command=Check, takefocus=False)
    CheckButton.place(x=20,y=17)

    L1.focus()

    

def Restart():
    for w in MainWindow.winfo_children():
        w.destroy()
    global yval
    yval = 120
    create()
    global guess
    guess = []
    global answer
    answer = []
    global word
    word = random.choice(words).upper()
    answer.append(word[0])
    answer.append(word[1])
    answer.append(word[2])
    answer.append(word[3])
    answer.append(word[4])
    global lives
    lives = 6


    



Restart()
MainWindow.mainloop()
#doc.close()



