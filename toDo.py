from tkinter import filedialog, Tk, Button, Frame, BOTTOM, Label, RIGHT, LabelFrame, Checkbutton, LEFT, Toplevel, Entry, \
    filedialog, END

root = Tk()
root.title("To Do App")
layout = LabelFrame(root)  ## layout=Frame(root) is the same. label frame just shows us the borders of the frame.

root.geometry("400x400")
root.configure(bg="lightblue")
layout.rowconfigure(0, weight=1)

layout.columnconfigure(0, weight=1)
layout.columnconfigure(1, weight=1)
ab = None
text=[]
y = 40
list = []



def open_list():
   global line


   file_path= file=filedialog.askopenfilename()
   '''
   file=open(file_path,'r')
   print((file.read()))
   '''
   with open(file_path, 'r') as file:
        global list2
        global text
        a = 0
        # Iterate over the lines of the file
        for line in file:
            # Process each line as needed
            print(line.strip())  # strip() removes leading and trailing whitespaces, including the newline character
            global y
            global ab
            y += 20

            button1 = Checkbutton(text=line.strip())

            list.append(button1)
            text.append(line.strip())
            button1.place(x=3, y=y)




def save_list():
  file=filedialog.asksaveasfile()
  for i in range(len(text)):
   file.write(text[i]+"\n")


def delete_all():

    for i in range(len(list)):
        a = list[i].destroy()


def delete_index(a):
    global line
    st = a.split(',')

    for x in range(len(st)):
        list[int(st[x])].destroy()


def button_command():
    global y
    global ab
    y += 20

    button1 = Checkbutton(text=ab.get())



    button1.place(x=3, y=y)
    list.append(button1)
    text.append(ab.get())



def add():
    global ab
    global text
    new_window = Toplevel()
    new_window.configure(bg="lightblue")

    new_window.geometry("300x300")
    label = Label(new_window, text="Enter a task to do ")
    label.configure(bg="purple")
    label.pack()
    entry = Entry(new_window)
    entry.pack()
    ab = entry



    button = Button(new_window, text="Add", command=button_command)
    button.pack()
    button.configure(bg="blue")


def delete():
    new_frame = Toplevel()
    new_frame.geometry("300x300")
    new_frame.configure(bg="lightblue")

    label = Label(new_frame, text="Enter indexes of lines you want to delete ")
    label.pack()
    label.configure(bg="purple")
    entry = Entry(new_frame)
    entry.pack()
    ab = entry

    button = Button(new_frame, text="Delete All", command=delete_all)
    button.pack()
    button.configure(bg="yellow")

    button = Button(new_frame, text="Delete By Indexes", command=lambda: delete_index(entry.get()))
    button.pack()
    button.configure(bg="blue")


label = Label(text="To Do List", font=("Arial", 18))
label.pack()
label.configure(bg="yellow")
layout.pack(fill="x", side=BOTTOM)

save_button = Button(root, text="Save", command=save_list)
#save_button.place(x=324,y=330)
save_button.pack(side=RIGHT,anchor='se')


save_button.configure(bg="yellow")

open_button = Button(root, text="Open", command=open_list)
#open_button.place(x=360,y=330)
open_button.pack(side=RIGHT,anchor='se')

open_button.configure(bg="blue")


add_button = Button(layout, text="ADD", font=("Arial", 15), command=add)
add_button.grid(row=0, column=0, sticky='we')

add_button.configure(bg="blue")

add_button1 = Button(layout, text="DELETE", font=("Arial", 15), command=delete)
add_button1.grid(row=0, column=1, sticky='we')
add_button1.configure(bg="yellow")


root.mainloop()
