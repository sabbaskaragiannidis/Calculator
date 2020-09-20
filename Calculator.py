# A programm in python using Tkinter
# to create a calculator

# Import everything from Tkinter
from tkinter import *

# Declare the expression variable globally
expression = ""


# Function update the expression
def press(num):
    global expression

    # Connection of string
    expression = expression + str(num)

    # Update the expression by using set method
    equation.set(expression)


# Evaluation of the final expression
def equal():
    # Handling the errors like zero
    # of division error
    try:
        global expression
        # Convert the result into string
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ImportError:
        equation.set(" error ")
        expression = ""


# Erase the errors in the entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Main code
# Creation of the window
g = Tk()
# Set a colour for the background of the window
g.configure(background="blue")
# Giving a title
g.title("Calculator")
# Configure the window
g.geometry("240x160")

equation = StringVar()

# create the entry box to show the expression
expression_field = Entry(g, textvariable=equation)

# this method is used to place the widgets
# at respective positions in the table
expression_field.grid(columnspan=4, padx=55, pady=6)

# create a Buttons and place at particular
# location inside the window.
# when user press the button, the command or
# function affiliated to that button is executed.
button1 = Button(g, text=' 1 ', fg='white', bg='black',
                 command=lambda: press(1), height=1, width=5)
button2 = Button(g, text=' 2 ', fg='white', bg='black',
                 command=lambda: press(2), height=1, width=5)
button3 = Button(g, text=' 3 ', fg='white', bg='black',
                 command=lambda: press(3), height=1, width=5)
button4 = Button(g, text=' 4 ', fg='white', bg='black',
                 command=lambda: press(4), height=1, width=5)
button5 = Button(g, text=' 5 ', fg='white', bg='black',
                 command=lambda: press(5), height=1, width=5)
button6 = Button(g, text=' 6 ', fg='white', bg='black',
                 command=lambda: press(6), height=1, width=5)
button7 = Button(g, text=' 7 ', fg='white', bg='black',
                 command=lambda: press(7), height=1, width=5)
button8 = Button(g, text=' 8 ', fg='white', bg='black',
                 command=lambda: press(8), height=1, width=5)
button9 = Button(g, text=' 9 ', fg='white', bg='black',
                 command=lambda: press(9), height=1, width=5)
button0 = Button(g, text=' 0 ', fg='white', bg='black',
                 command=lambda: press(0), height=1, width=5)
plus = Button(g, text=' + ', fg='white', bg='black',
              command=lambda: press("+"), height=1, width=5)
minus = Button(g, text=' - ', fg='white', bg='black',
               command=lambda: press("-"), height=1, width=5)
multiply = Button(g, text=' * ', fg='white', bg='black',
                  command=lambda: press("*"), height=1, width=5)
divide = Button(g, text=' / ', fg='white', bg='black',
                command=lambda: press("/"), height=1, width=5)
equal = Button(g, text=' = ', fg='white', bg='black',
               command=equal, height=1, width=5)
clear = Button(g, text='Clear', fg='white', bg='black',
               command=clear, height=1, width=5)


button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
button0.grid(row=5, column=0)
plus.grid(row=2, column=3)
minus.grid(row=3, column=3)
multiply.grid(row=4, column=3)
divide.grid(row=5, column=3)
equal.grid(row=5, column=2)
clear.grid(row=5, column='1')

# start
g.mainloop()
