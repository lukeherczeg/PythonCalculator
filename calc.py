from tkinter import*

def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)

def buttonClearDisplay():
    global operator
    operator = ""
    textInput.set("")

def buttonEqualsParse():
    global operator
    result = str(eval(operator))
    textInput.set(result)
    operator = ""

def keyBindEqualsParse(event):
    result = str(eval(textInput.get()))
    textInput.set(result)

def keyBindClearParse(event):
    textInput.set("")


cal = Tk()
cal.title("Luke's Handy Calc")
operator = ""
textInput = StringVar()

cal.bind("<Return>", keyBindEqualsParse)
cal.bind("C", keyBindClearParse)

textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable = textInput,
bd = 5, insertwidth = 6, bg = "#00ffff", justify = 'right').grid(columnspan=4)

##================================= Buttons =======================================
#==================================================================================
#==================================================================================

button7 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "7", command = lambda:buttonClick(7)).grid(row = 1, column = 0)

button8 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "8", command = lambda:buttonClick(8)).grid(row = 1, column = 1)

button9 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "9", command = lambda:buttonClick(9)).grid(row = 1, column = 2)

addbutton = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "+", command = lambda:buttonClick("+")).grid(row = 1, column = 3)

#==================================================================================

button4 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "4", command = lambda:buttonClick(4)).grid(row = 2, column = 0)

button5 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "5", command = lambda:buttonClick(5)).grid(row = 2, column = 1)

button6 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "6", command = lambda:buttonClick(6)).grid(row = 2, column = 2)

subbutton = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "-", command = lambda:buttonClick("-")).grid(row = 2, column = 3)

#==================================================================================

button4 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "1", command = lambda:buttonClick(1)).grid(row = 3, column = 0)

button5 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "2", command = lambda:buttonClick(2)).grid(row = 3, column = 1)

button6 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "3", command = lambda:buttonClick(3)).grid(row = 3, column = 2)

multbutton = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "*", command = lambda:buttonClick("*")).grid(row = 3, column = 3)

#==================================================================================

button4 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "0", command = lambda:buttonClick(0)).grid(row = 4, column = 0)

button5 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "C", command = lambda:buttonClearDisplay()).grid(row = 4, column = 1)

button6 = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "=", command = lambda:buttonEqualsParse()).grid(row = 4, column = 2)

divbutton = Button(cal, padx = 15, bd = 5, bg = "#00ffff", fg = "black",  font=('arial', 20, 'bold'),
text = "/", command = lambda:buttonClick("/")).grid(row = 4, column = 3)




cal.mainloop()
