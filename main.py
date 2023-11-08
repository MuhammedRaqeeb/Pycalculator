#simple GUI CALCULATOR using python

import tkinter as tk  
from tkinter import messagebox


calculation = ""
def add_calculation(symbol): # defining the calculation
    global calculation 
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():  
    global calculation
    
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:   
        clear_field()
        text_result.insert(1.0, "ERROR" ) 
        
def clear_field():
    global calculation 
    calculation = ""
    text_result.delete(1.0 , "end")

def close_window(): # using messagebox for destroy the window
    response = messagebox.askquestion("Quit" , "Do You Really Want To Quit ?")   
    if response == "yes":
        root.destroy()
    else:
        pass
           
root = tk.Tk()

root.geometry("420x450") # size of the window

#output window
text_result = tk.Text(root , height=2 , width=22 , font=('ARIAL' , 24))
text_result.grid(columnspan=7)

#bottom label
label = tk.Label(root , text="Welcome" , width=10 ,font=('Comic Sans MS' , 30 )  ,fg='#006400' , background='#FFD39B' , padx=150 , pady=5)
label.place(  relx=0.5,rely=1 , anchor='s' )

#button 
btn1 = tk.Button(root , text = "1" , command=lambda: add_calculation(1) , width=5 , font=('Arial' , 24)  , activebackground='yellow')
btn1.grid(row=2 , column= 0) 


btn2 = tk.Button(root , text = "2" , command=lambda: add_calculation(2) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn2.grid(row=2 , column= 1) 


btn3 = tk.Button(root , text = "3" , command=lambda: add_calculation(3) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn3.grid(row=2 , column= 2) 


btn4 = tk.Button(root , text = "4" , command=lambda: add_calculation(4) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn4.grid(row=3 , column= 0) 


btn5 = tk.Button(root , text = "5" , command=lambda: add_calculation(5) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn5.grid(row=3 , column= 1) 


btn6 = tk.Button(root , text = "6" , command=lambda: add_calculation(6) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn6.grid(row=3 , column= 2) 


btn7 = tk.Button(root , text = "7" , command=lambda: add_calculation(7) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn7.grid(row=4 , column= 0) 


btn8 = tk.Button(root , text = "8" , command=lambda: add_calculation(8) , width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn8.grid(row=4 , column= 1)


btn9 = tk.Button(root , text = "9" , command=lambda: add_calculation(9) , width=5 , font=('Arial' , 24) , activebackground='yellow')
btn9.grid(row=4 , column= 2) 


btn0 = tk.Button(root , text = "0" ,command=lambda:add_calculation(0), width=5 , font=('Arial' , 24) ,  activebackground='yellow')
btn0.grid(row=5 , column= 1) 


btn_plus = tk.Button(root , text = "+" , command=lambda: add_calculation("+") , width=5 , font=('Arial' , 24) ,   activebackground='skyblue')
btn_plus.grid(row=2 , column= 3) 


btn_minus = tk.Button(root , text = "-" , command=lambda: add_calculation("-") , width=5 , font=('Arial' , 24) ,  activebackground='skyblue')
btn_minus.grid(row=3 , column= 3) 


btn_division = tk.Button(root , text = "/" , command=lambda: add_calculation("/") , width=5 , font=('Arial' , 24) ,  activebackground='skyblue')
btn_division.grid(row=4 , column= 3) 


btn_multiply = tk.Button(root , text = "*" , command=lambda: add_calculation("*") , width=5 , font=('Arial' , 24) ,  activebackground='skyblue')
btn_multiply.grid(row=5 , column= 3) 


btn_open = tk.Button(root , text = "(" , command=lambda: add_calculation("(") , width=5 , font=('Arial' , 24) ,  activebackground='skyblue')
btn_open.grid(row=5 , column= 0) 

btn_close = tk.Button(root , text = ")" , command=lambda: add_calculation(")") , width=5 , font=('Arial' , 24) , activebackground='skyblue')
btn_close.grid(row=5 , column= 2) 

btn_clear= tk.Button(root , text = "C" , command=clear_field , width=5 , font=('Arial' , 24) ,  activebackground='skyblue')
btn_clear.grid(row=6 , column= 1) 

btn_equal = tk.Button(root , text = "=" , command=evaluate_calculation , width=5 , font=('Arial' , 24) ,  activebackground='green')
btn_equal.grid(row=6 , column= 3) 

btn_point= tk.Button(root , text = "." , command=lambda:add_calculation(".") , width=5 , font=('Arial' , 24) ,  activebackground='skyblue')
btn_point.grid(row=6 , column= 2) 

 #quit button for closing the window    
btn_quit = tk.Button(root, text="Quit" , command=close_window   , width=5 , font=('Arial' , 24) ,  activebackground='red')
btn_quit.grid(column=0, row=6)       

root.mainloop()

