import os as o
import shutil
import tkinter as tk
from tkinter import filedialog,messagebox

try:
    file = None


    def show_files():
        show = filedialog.askopenfile()


    def delete_files():
        try:


            global file

            print(selected_value.get())
            file = filedialog.askdirectory()
            print(file)
            files = o.listdir(str(file))
            print(files)

            specific_operation = bool(selected_value.get())
            if not specific_operation:
                print("Deleting all files in the directory.")
                for i in range(len(files)):

                      if  o.path.isdir(file + "/" + files[i]):
                           shutil.rmtree(file + "/" + files[i])
                      if o.path.isfile(file+"/"+files[i]):
                           o.remove(file + "/" + files[i])


            else:
                print(f"Deleting {selected_value.get()} files.")
                for i in range(len(files)):
                    a = files[i].split('.')
                    if a[len(a) - 1] == selected_value.get():
                      if  o.path.isdir(file + "/" + files[i]):
                           shutil.rmtree(file + "/" + files[i])
                      if o.path.isfile(file+"/"+files[i]):
                           o.remove(file + "/" + files[i])
            selected_value.set('')

        except Exception as e:
            print(e)


    extension_list = []


    def category_files():
        try:
            specific_operation = bool(selected_value.get())
            global file
            file = filedialog.askdirectory()
            files = o.listdir(str(file))
            filess = o.listdir(file)
            ## adding file extensions in a list.
            for i in range(len(files)):
                split = files[i].split('.')
                if split[len(split) - 1] not in extension_list:
                    extension_list.append(split[len(split) - 1])

            if not specific_operation:
                for k in range(len(extension_list)):
                    new_folder_path = o.path.join(file, extension_list[k])
                    file_path = o.path.join(file, filess[k])

                    if not o.path.exists(new_folder_path):
                        print(f"Creating new folder path: {new_folder_path}")
                        o.makedirs(file + "/" + extension_list[k])

                for j in range(len(files)):
                    split = files[j].split('.')
                    shutil.move(file + "/" + filess[j], file + "/" + split[len(split) - 1])
            else:
                print(f"Grouping files in a folder: {selected_value.get()}")
                new_folder_path = o.path.join(file, selected_value.get())
                file_path = o.path.join(file, selected_value.get())
                print(f"New folder path: {new_folder_path}")
                if not o.path.exists(new_folder_path):
                    print("Creating folder.")
                    o.makedirs(file + "/" + selected_value.get())

                for j in range(len(files)):
                    split = files[j].split('.')
                    if split[len(split) - 1] == selected_value.get():
                        shutil.move(file + "/" + filess[j], file + "/" + split[len(split) - 1])
            selected_value.set('')
        except Exception as e:

            messagebox.showinfo(title="Error",message= f" {e}")




    def selected_value_changed(*args):
        category_button.config(text=f"Group {selected_value.get()} Files in a Folder")
        button.config(text=f"Select a Directory to Delete All {selected_value.get()} Files")


    root = tk.Tk()

    file_types = [
        '',"txt", "csv",
        "doc", "docx", "pdf",
        "xls", "xlsx",
        "jpg", "jpeg", "png", "gif",
        "ppt", "pptx",
        "sqlite", "mdb",
        "py", "java", "html", "css",
        "exe", "app",
        "zip",
        "mp3", "wav", "rar"
    ]
    selected_value = tk.StringVar(root)

    label = tk.Label(root, text="Select a File Type You Want to Perform an Operation", font=("Helvetica", 12))
    label.pack(pady=10)
    label.configure(background="yellow")

    dp_menu = tk.OptionMenu(root, selected_value, *file_types)
    dp_menu.pack(pady=10)
    dp_menu.configure(font=('Helvetica', 10), background='blue', foreground='white', relief=tk.GROOVE)

    button_show = tk.Button(root, text="Show Files", command=show_files, font=("Helvetica", 10),
                            bg='#4CAF50', fg='white', relief=tk.GROOVE)
    button_show.pack(pady=20)

    button = tk.Button(root, text="Select a Directory to Delete Files", command=delete_files, font=("Helvetica", 10),
                       bg='#4CAF50', fg='white', relief=tk.GROOVE)
    button.pack(pady=20)

    category_button = tk.Button(root, text="Group Files in Separate Folders", command=category_files,
                                font=("Helvetica", 10), bg='#008CBA', fg='white', relief=tk.GROOVE)
    category_button.pack(pady=20)

    selected_value.trace("w", selected_value_changed)

    root.geometry("400x400")
    root.title("File Organizer")
    root.configure(background='lightblue')
    root.mainloop()

except Exception as e:
    print(f"An error occurred: {e}")
