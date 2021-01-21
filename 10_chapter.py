#10 - Practicum. Виселица   02.12.20
import random
"""
#first we create function, where whole game is locating
def hangman(word):
    wrong=0
    stages=["",
            " _______________         ",
            " |                       ",
            " |             |         ",
            " |             0         ",
            " |            /|\        ",
            " |            / \        ",
            " |                       "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Добро пожаловать на казнь!")

#making a loop, providing gameplay
    while wrong < len(stages)-1:
        print("\n")
        msg="Введите букву: "
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово:{}.".format(word))

hangman("даква")
"""





#practicum
#change the game in such way, that word is selected from word list.

def hangman(word):
    wrong=0
    stages=["",
            " _______________         ",
            " |                       ",
            " |             |         ",
            " |             0         ",
            " |            /|\        ",
            " |            / \        ",
            " |                       "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Добро пожаловать на казнь!")
    while wrong < len(stages)-1:
        print("\n")
        msg="Введите букву: "
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово:{}.".format(word))

wordlist=["даурен","даир","адиль","алиш","бира","адлет","дастан","мага","алуа","малика","марьям"]
n=len(wordlist)
rand=random.randint(0,n)

hangman(wordlist[rand])
