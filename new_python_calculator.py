from tkinter import *
root = Tk()
root.title("Python Calculator")

#globally declare the operator variable
operator = ""
text_input = StringVar()
e = Entry(root, font = ('arial', 20, 'bold'), textvariable = text_input, bd = 15,insertwidth = 4, bg = "powder blue",justify = 'right')
e.grid( columnspan = 4)


def button_click(number):
   
   #point out the global variable
   global operator
   
   operator = operator + str(number) #concatenation of string
   
   text_input.set(operator) #updating the operator using set method
   
def button_equal():
   try:
     global operator
     sumup = str(eval(operator))
     text_input.set(sumup)
     operator = ""
   except:
      text_input.set(" error ")
      operator = ""

  
   
def button_clear():
   global operator
   operator = ""
   text_input.set("")
   # e.delete(0, END)


#create or define buttons
button_1 = Button(root, text = "1", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black', bg = "powder blue",command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click(3))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
button_4 = Button(root, text = "4", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black', bg = "powder blue",command = lambda: button_click(6))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
button_7 = Button(root, text = "7", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black', bg = "powder blue",command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click(9))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
button_0 = Button(root, text = "0", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black', bg = "powder blue",command = lambda: button_click(0))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

button_add = Button(root, text = "+", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black', bg = "powder blue",command = lambda: button_click('+'))
button_sub = Button(root, text = "-", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = lambda: button_click('-'))
button_mul = Button(root, text = "*", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command =lambda: button_click('*'))
button_div = Button(root, text = "/", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black', bg = "powder blue",command = lambda: button_click('/'))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

button_equal = Button(root, text = "=", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = button_equal)
button_clear = Button(root, text = "c", padx = 16, pady = 16, bd = 8, font = ('arial',20,'bold'),fg ='black',bg = "powder blue", command = button_clear)

#put the buttons on the screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 1, column = 3)
button_sub.grid(row = 2, column = 3)
button_mul.grid(row = 3, column = 3)
button_div.grid(row = 4, column = 3)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row = 4, column = 1)



root.mainloop()

