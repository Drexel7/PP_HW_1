
# Python program to  create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""



# Function to update expressiom
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression
        nrop = 0
        stiva = []
        coada = []
        cifre = "0123456789"
        operatori = "+-*/"

        i = 1
        while i < len(expression):
            if expression[i] not in cifre and expression[i - 1] in cifre:
                expression = expression[:i] + ' ' + expression[i:]
                i = i + 1
            i = i + 1
        if expression[len(expression) - 1] in cifre:
            expression = expression + ' '
        for i in range(len(expression)):
            ch = expression[i]
            if ch == '(':
                stiva.append(ch)
            if ch in cifre:
                coada.append(ch)
            if ch == ')':
                ci = len(stiva) - 1
                while stiva[ci] != '(':
                    elem = stiva.pop()
                    coada.append(elem)
                    ci = ci - 1
                stiva.pop()
            if ch in operatori:
                nrop = nrop + 1
                if len(stiva) == 0 or priority(ch) > priority(stiva[-1]) :
                    stiva.append(ch)
                else:
                    while len(stiva) != 0 and priority(ch) <= priority(stiva[-1]) and stiva[-1] != '(' and stiva: #verific daca stiva e goala
                        elem = stiva.pop()
                        coada.append(elem)
                    stiva.append(ch)
            if ch == ' ':
                coada.append(ch)
        while stiva:
            elem = stiva.pop()
            coada.append(elem)

        for i in range(len(coada)):
            if coada[i] == ' ' and coada[i-1] not in cifre:
                coada.pop(i)



        i = 0
        while nrop != 0 :
            if coada[i] in operatori:
                ci = i - 2
                nr1 = 0
                nrc1 = 0 #nrcifre
                while coada[ci] != ' ' and ci > 0:
                    ci = ci - 1
                #daca am ajuns aici atunci se termina un numar
                cix = ci + 1
                while cix < i - 1:
                    nr1 = nr1 * 10 + int(coada[cix])
                    nrc1 = nrc1 + 1
                    cix = cix + 1

                nr2 = 0
                nrc2 = 0
                cix = ci - 1
                while coada[cix] != ' ' and cix > 0:
                    cix = cix - 1
                #daca am ajuns aici atunci se termina un numar
                if cix != 0:
                    cix = cix + 1
                ccix = cix #tin minte unde sa pun rezultatul operatiei

                while cix < ci:
                    nr2 = nr2 * 10 + int(coada[cix])
                    nrc2 = nrc2 + 1
                    cix = cix + 1
                if coada[i] == '+':
                    nr = nr2 + nr1
                if coada[i] == '-':
                    nr = nr2 - nr1
                if coada[i] == '*':
                    nr = nr2 * nr1
                if coada[i] == '/':
                    nr = nr2 / nr1
                    nr = int(nr)

                nrc = len(str(nr))#nr cifre

                #modific sirul de caractere din coada

                nrp = nrc1 + 1 + nrc2 + 1 + 1#spatiul pt nrc1 + spatiu nrc2 + semnul


                while nrp != 0:
                    coada.pop(ccix)
                    nrp = nrp - 1
                nrs = str(nr) #fac string
                siraux = ""
                for x in range(ccix):
                    siraux += coada[x]
                siraux += nrs + ' '
                for x in range(ccix,len(coada)):
                    siraux += coada[x]



                coada = []
                j = 0
                while j < len(siraux):
                    coada.append(siraux[j])
                    j = j + 1

                nrop = nrop - 1

                i = i - (nrc1 + nrc2 + 1 + 1 - nrc - 1)

            else:
                i = i + 1

        total = ""
        for i in range(len(coada)):
            total += coada[i]
        equation.set(total)


        # initialze the expression variable
        # by empty string
        expression = ""

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""








    # Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

def priority(ch):
    if ch == '(' or ch == ')':
        return 2;
    if ch == '*' or ch == '/':
        return 1;
    if ch == '+' or ch == '-':
        return 0;





# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="gray")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("340x140")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .

    button1 = Button(gui, text=' 1 ', fg='white', bg='blue',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='blue',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='blue',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='white', bg='blue',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='blue',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='blue',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='white', bg='blue',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='blue',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='blue',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='blue',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='white', bg='blue',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='blue',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='white', bg='blue',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='blue',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='blue',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    leftparanthesis = Button(gui, text =' ( ', fg = 'white', bg = 'blue',
                            command = lambda: press("("),height = 1, width = 7)
    leftparanthesis.grid(row=2, column=4)

    rightparanthesis = Button(gui, text =' ) ', fg = 'white', bg = 'blue',
                             command = lambda: press(")"),height = 1, width = 7)
    rightparanthesis.grid(row=3, column=4)

    clear = Button(gui, text='Clear', fg='white', bg='blue',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    # start the GUI
    gui.mainloop()
