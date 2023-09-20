import tkinter
from tkinter import *
from tkinter import ttk

## colours
c0, c1, c2, c4, c7, background = "#FFFFFF", "#000025", "#fcc058", "#3297a8", "#e85151", "#000030"
c8 = c4 

## first window
# Tk() inform what is the first window 
window = Tk()
window.title('Hello!')
window.geometry('270x400')
# window colour
window.configure(bg=background)

## split the first window in two sections
# shading - relief="raised"
# note: bg means background
Frame_top = Frame(window, width=250, height=100, bg=c1, relief="raised")        

# position - top left corner - sticky=NW
# width, height of inside elements - padx=10, pady=10
# .grid() create a table
Frame_top.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

Frame_bottom = Frame(window, width=250, height=300, bg=background, relief="flat")        
Frame_bottom.grid(row=1, column=0, sticky=NW, padx=10, pady=10)

### configure Frame_top
## first player punctuation
# note: fg means foreground
# Label() display boxes with text or images
app_x = Label(Frame_top, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=c1, fg=c7)
# X position
app_x.place(x=25, y=10)

# text
app_x = Label(Frame_top, text='Player 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=c1, fg=c0)
app_x.place(x=25, y=70)

# punctuation
punc_x = Label(Frame_top, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=c1, fg=c0)
punc_x.place(x=85, y=15)

app_separador = Label(Frame_top, text=':', height=1, relief='flat', anchor='center', font=('Ivy 20 bold'), bg=c1, fg=c0)
app_separador.place(x=115, y=20)

## second player punctuation
app_o = Label(Frame_top, text='0', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=c1, fg=c4)
app_o.place(x=175, y=10)
app_o = Label(Frame_top, text='Player 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=c1, fg=c0)
app_o.place(x=175, y=70)
punc_o = Label(Frame_top, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=c1, fg=c0)
punc_o.place(x=130, y=15)

### create the two players and the game logic
player_1, player_2 = "X", "0"

## initial score
score_1, score_2 = 0, 0

# 3d array
table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# will start with the X player
playing, pointsCounter, roundCounter = 'X', 0, 0

#### main function
def init_game():
    b_play.place(x=850, y=350)
    
    # controle the game
    def controle(i):
        # which player is currently playing
        global playing
        # count the current points
        global pointsCounter

        # compare the value received
        if i==str(1):
            # check if that position is empty
            if b_0['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_0['fg'] = colour
                # defined the text
                b_0['text'] = playing
                # save in the array the symbol of the player
                table[0][0] = playing

                # see who's playing, in order to change the player
                if playing == 'X': 
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(2):
            # check if that position is empty
            if b_1['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_1['fg'] = colour
                # defined the text
                b_1['text'] = playing
                # save in the array the symbol of the player
                table[0][1] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(3):
            # check if that position is empty
            if b_2['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_2['fg'] = colour
                # defined the text
                b_2['text'] = playing
                # save in the array the symbol of the player
                table[0][2] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(4):
            # check if that position is empty
            if b_3['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_3['fg'] = colour
                # defined the text
                b_3['text'] = playing
                # save in the array the symbol of the player
                table[1][0] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(5):
            # check if that position is empty
            if b_4['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_4['fg'] = colour
                # defined the text
                b_4['text'] = playing
                # save in the array the symbol of the player
                table[1][1] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(6):
            # check if that position is empty
            if b_5['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_5['fg'] = colour
                # defined the text
                b_5['text'] = playing
                # save in the array the symbol of the player
                table[1][2] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(7):
            # check if that position is empty
            if b_6['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_6['fg'] = colour
                # defined the text
                b_6['text'] = playing
                # save in the array the symbol of the player
                table[2][0] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(8):
            # check if that position is empty
            if b_7['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_7['fg'] = colour
                # defined the text
                b_7['text'] = playing
                # save in the array the symbol of the player
                table[2][1] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        if i==str(9):
            # check if that position is empty
            if b_8['text']=='':
                # see who's playing
                if playing == 'X': colour=c7
                if playing == 'O': colour=c8

                # defined the text colour button
                b_8['fg'] = colour
                # defined the text
                b_8['text'] = playing
                # save in the array the symbol of the player
                table[2][2] = playing

                # see who's playing, in order to change the player
                if playing == 'X':
                    playing = 'O'
                else:
                    playing = 'X'

                # INCREMENT THE COUNTER
                pointsCounter+=1

        # after the counter is equal or higher than 5, verify if we have a winner
        if pointsCounter>=5:
            # lines
            if table[0][0] == table[0][1] == table[0][2] != "":
                winner(playing)
            elif table[1][0] == table[1][1] == table[1][2] != "":
                winner(playing)
            elif table[2][0] == table[2][1] == table[2][2] != "":
                winner(playing)

            # colunms
            if table[0][0] == table[1][0] == table[2][0] != "":
                winner(playing)
            elif table[0][1] == table[1][1] == table[2][1] != "":
                winner(playing)
            elif table[0][2] == table[1][2] == table[2][2] != "":
                winner(playing)

            # diagonal
            if table[0][0] == table[1][1] == table[2][2] != "":
                winner(playing)
            elif table[0][2] == table[1][1] == table[2][0] != "":
                winner(playing)

            # tie
            if pointsCounter>=9:
                winner("It´s tie!")

    # decide who is the winner
    def winner(i):
        global table
        global score_1
        global score_2
        global roundCounter
        global pointsCounter

        b_0['state'], b_1['state'], b_2['state'], b_3['state'], b_4['state'] = 'disable', 'disable', 'disable', 'disable', 'disable'
        b_5['state'], b_6['state'], b_7['state'], b_8['state']  = 'disable', 'disable', 'disable', 'disable'

        app_winner = Label(Frame_bottom, text='', width=14, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=background, fg=c2)
        app_winner.place(x=40, y=185)

        if i=='X':
            score_2+=1
            app_winner['text']='Player 2 win!'
            punc_o['text']=score_2

        if i=='O':
            score_1+=1
            app_winner['text']='Player 1 win!'
            punc_x['text']=score_1

        if i=="It´s tie!":
            app_winner['text']='It´s tie!'

        def start():
            # clean the buttons
            b_0['text'], b_1['text'], b_2['text'], b_3['text'], b_4['text']='', '', '', '', ''
            b_5['text'], b_6['text'], b_7['text'], b_8['text']='', '', '', ''

            b_0['state'], b_1['state'], b_2['state'], b_3['state'], b_4['state'] = 'normal', 'normal', 'normal', 'normal', 'normal'
            b_5['state'], b_6['state'], b_7['state'], b_8['state']  = 'normal', 'normal', 'normal', 'normal'

            app_winner.destroy()
            b_play.destroy()

        b_play = Button(Frame_bottom, command=start, text='Next game!', width=10, height=1, font=('Ivy 10 bold'), relief='raise', bg=background, fg=c7)
        b_play.place(x=85, y=215)

        def endGame():
            b_play.destroy()
            app_winner.destroy()
            end()

        if roundCounter>=5:
            endGame()
        else:
            roundCounter+=1
            # restart the table array
            table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            pointsCounter = 0

    # end the game
    def end():
        global table
        global roundCounter
        global score_1
        global score_2
        global pointsCounter

        table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        roundCounter, score_1, score_2, pointsCounter = 0, 0, 0, 0

        b_0['state'], b_1['state'], b_2['state'], b_3['state'], b_4['state'] = 'disable', 'disable', 'disable', 'disable', 'disable'
        b_5['state'], b_6['state'], b_7['state'], b_8['state']  = 'disable', 'disable', 'disable', 'disable'

        app_end = Label(Frame_bottom, text='End game!', width=14, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=background, fg=c2)
        app_end.place(x=40, y=90)

        def play_again():
            punc_x['text']='0'
            punc_o['text']='0'
            app_end.destroy()
            b_play.destroy()
            init_game()

        b_play = Button(Frame_bottom, command=play_again, text='Play', width=10, height=1, font=('Ivy 10 bold'), relief='raise', bg=background, fg=c7)
        b_play.place(x=85, y=215)   

    ## vertical lines
    app_ = Label(Frame_bottom, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=c0, fg=c7)
    app_.place(x=90, y=15)
    app_ = Label(Frame_bottom, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=c0, fg=c7)
    app_.place(x=160, y=15)

    ## horizontal lines
    app_ = Label(Frame_bottom, text=' ', width=190, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=c0, fg=c7)
    app_.place(x=30, y=63)
    app_ = Label(Frame_bottom, text=' ', width=190, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=c0, fg=c7)
    app_.place(x=30, y=123)

    ### configure Frame_bottom
    ## line 0
    # note: lambda arguments : expression
    # A lambda function can take any number of arguments, but can only have one expression
    b_0 = Button(Frame_bottom, command=lambda:controle('1'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_0.place(x=30, y=15)
    b_1 = Button(Frame_bottom, command=lambda:controle('2'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_1.place(x=100, y=15)
    b_2 = Button(Frame_bottom, command=lambda:controle('3'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_2.place(x=170, y=15)

    ## line 1
    b_3 = Button(Frame_bottom, command=lambda:controle('4'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_3.place(x=30, y=73)
    b_4 = Button(Frame_bottom, command=lambda:controle('5'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_4.place(x=100, y=73)
    b_5 = Button(Frame_bottom, command=lambda:controle('6'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_5.place(x=170, y=73)

    ## line 2
    b_6 = Button(Frame_bottom, command=lambda:controle('7'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_6.place(x=30, y=133)
    b_7 = Button(Frame_bottom, command=lambda:controle('8'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_7.place(x=100, y=133)
    b_8 = Button(Frame_bottom, command=lambda:controle('9'), text='', width=3, font=('Ivy 17 bold'), relief='flat', bg=background, fg=c7)
    b_8.place(x=170, y=133)

### play button
# note: command=init_game - when the button play is clicked, display the function
b_play = Button(Frame_bottom, command=init_game, text='Play', width=10, height=1, font=('Ivy 10 bold'), relief='raise', bg=background, fg=c7)
b_play.place(x=85, y=215)


window.mainloop()                    
                    
                    

