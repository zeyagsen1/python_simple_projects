import tkinter
import tkinter as tk
from tkinter import *


memory=""
first=None
second=None
newstrr=""
signs= ""

def button_click(k):
  result=0
  global memory
  global first
  global second
  global newstrr
  global signs
  global multiply

  part_two_active=False
  if k!=13:
   text.insert(END,k)



  if k=="x" or k=='-'or k=='/'or k=='+':
      modified_string = memory.replace(k, '')
      print('modified string =' + modified_string)
      first=modified_string
      signs=k



  else:



      if k!=13:
       memory = text.get()
       print(memory)

  if k==13:
   sum=0
   f=1
   only_numbers = memory.split(signs)
   numbers_length=len(only_numbers)

   p=0
   a=0
   t=0
   multiply=1
   for i in range(numbers_length):
    if signs== '+':
        sum=sum+int(only_numbers[i])
        print(sum)

    if signs== '-'and i<numbers_length-1:
     if t==0:
       a+=int(only_numbers[i])-int(only_numbers[i+1])
       t=1
     else:
       a-=int(only_numbers[i+1])

    if signs=='x':
        multiply*=int(only_numbers[i])
        print(multiply)

    if signs== '/'and i<numbers_length-1:
     if t==0:


       a+=int(only_numbers[i])/int(only_numbers[i+1])
       t=1
     else:
       print(only_numbers[i])

       a/=int(only_numbers[i+1])





frame = tk.Tk()

frame.geometry("500x500")

label = tk.Label(frame, text="CALCULATOR", font=('Arial', 15))
label.pack(padx=20, pady=20)

text = tk.Entry(frame, font=('Arial', 15))
text.pack(fill='x')

'''
textbox=tk.Entry(frame)
textbox.pack()

button=tk.Button(frame,text="Click Me")
button.pack()
'''
# side bottom sets the button's place as the most buttom of the frame

layout = Frame(frame)
layout.columnconfigure(0, weight=2)  ## weight indicates how much space that a column
layout.columnconfigure(1, weight=2)  ## will take. if all weights are the same
layout.columnconfigure(2, weight=1)  ##all of them take the same space.

btn1 = tk.Button(layout, text="1", font=("Arial", 18), command=lambda: button_click(1))
btn1.grid(row=0, column=0, sticky="we")

btn2 = tk.Button(layout, text="2", font=("Arial", 18), command=lambda: button_click(2))
btn2.grid(row=0, column=1, sticky="we")

btn3 = tk.Button(layout, text="3", font=("Arial", 18), command=lambda: button_click(3))
btn3.grid(row=0, column=2, sticky="we")

btn4 = tk.Button(layout, text="4", font=("Arial", 18), command=lambda: button_click(4))
btn4.grid(row=1, column=0, sticky="we")

btn5 = tk.Button(layout, text="5", font=("Arial", 18), command=lambda: button_click(5))
btn5.grid(row=1, column=1, sticky="we")

btn6 = tk.Button(layout, text="6", font=("Arial", 18), command=lambda: button_click(6))
btn6.grid(row=1, column=2, sticky="we")

btn7 = tk.Button(layout, text="7", font=("Arial", 18), command=lambda: button_click(7))
btn7.grid(row=2, column=0, sticky='we')

btn8 = tk.Button(layout, text="8", font=("Arial", 18), command=lambda: button_click(8))
btn8.grid(row=2, column=1, sticky='we')

btn9 = tk.Button(layout, text="9", font=("Arial", 18), command=lambda: button_click(9))
btn9.grid(row=2, column=2, sticky='we')

btn10 = tk.Button(layout, text="0", font=("Arial", 18), command=lambda: button_click(0))
btn10.grid(row=3, column=0, sticky='we')

btn11 = tk.Button(layout, text="+", font=("Arial", 18), command=lambda: button_click("+"))
btn11.grid(row=3, column=1, sticky='we')

btn12 = tk.Button(layout, text="-", font=("Arial", 18), command=lambda: button_click("-"))
btn12.grid(row=3, column=2, sticky='we')

btn13 = tk.Button(layout, text="x", font=("Arial", 18), command=lambda: button_click("x"))
btn13.grid(row=4, column=0, sticky='we')

btn14 = tk.Button(layout, text="/", font=("Arial", 18), command=lambda: button_click("/"))
btn14.grid(row=4, column=1, sticky='we')

btn15 = tk.Button(layout, text="Calculate", font=("Arial", 18), command=lambda: button_click(13))
##command helps us to call the function when we click on that button
##it does not take () as methods just takes the name of the fuction
##becuse of that when we need to put variables inside a method we call
## use lambda funtion
## so we say command=Lambda:button_click(5)
##instead command=button_click . we can not even add 5 when we use it.
btn15.grid(row=4, column=2, sticky='we')

layout.pack(fill='x', side=BOTTOM)

# fill=x stretch all items  to the x dimension

frame.mainloop()  # You should set frame things and then call mainloop to see it.

