from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import subprocess
import webbrowser
# create an instance for window
window = Tk()
# set title for window
window.title("Adipoli IDE")
# create and configure menu
menu = Menu(window)
window.config(menu=menu)

# create editor window for writing code
editor = ScrolledText(window, font=("courier 10 bold"), wrap=None, insertbackground='red')
editor.pack(fill=BOTH, expand=1)
editor.focus()
file_path = ""
# function to open files
def open_file(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    file_path = open_path    
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        for line in code:
            print("line")
window.bind("<Control-o>", open_file)
# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-s>", save_file)
# function to save files as specific name 
def save_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-S>", save_as)
# function to execute the code and
# display its output
def run(event=None):
    global code, file_path
    '''
    code = editor.get(1.0, END)
    exec(code)
    '''    
    cmd = f"python {file_path}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, error =  process.communicate()
    # delete the previous text from
    # output_windows
    output_window.delete(1.0, END)
    # insert the new output text in
    # output_windows
    output_window.insert(1.0, output)
    # insert the error text in output_windows
    # if there is error
    output_window.insert(1.0, error)
window.bind("<F5>", run)
# function to close IDE window
def close(event=None):
    window.destroy()
window.bind("<Control-q>", close)
# define function to cut 
# the selected text
def cut_text(event=None):
        editor.event_generate(("<<Cut>>"))
# define function to copy 
# the selected text
def copy_text(event=None):
        editor.event_generate(("<<Copy>>"))
# define function to paste 
# the previously copied text
def paste_text(event=None):
        editor.event_generate(("<<Paste>>"))
# create menus
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
html_menu = Menu(menu, tearoff=0)
cpp_menu = Menu(menu, tearoff=0)
# add menu labels
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label ="View", menu=view_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
menu.add_cascade(label ="HTML", menu=html_menu)
menu.add_cascade(label ="C++", menu=cpp_menu)
#C++ Extension engine
# function to open Cpp files
def OpenCpp(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Text File", "*.cpp")])
    file_path = open_path    
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        for line in code:
            print("line")
# function to save Cpp files as specific name 
def SaveCpp_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".cpp", filetypes=[("Cpp File", "*.cpp")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
# function to save Cpp files
def SaveCpp(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".cpp", filetypes=[("Cpp File", "*.cpp")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code)
# function to run cpp files
def RunCpp(event=None):
    global file_path
    webbrowser.open('file://' + file_path, new=2)      
#HTML Extension engine
# function to open HTML files
def OpenHTML(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Text File", "*.html")])
    file_path = open_path    
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        for line in code:
            print("line")
# function to save HTML files as specific name 
def SaveHTML_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".html", filetypes=[("HTML File", "*.html")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
# function to save HTML files
def SaveHTML(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".html", filetypes=[("HTML File", "*.html")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code)
# function to run html files
def RunHTML(event=None):
    global file_path
    webbrowser.open('file://' + file_path, new=2)      
# add commands for HTML menu
html_menu.add_command(label="Open HTML", command=OpenHTML)
html_menu.add_command(label="Save HTML", command=SaveHTML)
html_menu.add_command(label="Save HTML as", command=SaveHTML_as)
html_menu.add_command(label="Run HTML", command=RunHTML)
# add commands for Cpp menu
cpp_menu.add_command(label="Open Cpp", command=OpenCpp)
cpp_menu.add_command(label="Save Cpp", command=SaveCpp)
cpp_menu.add_command(label="Save Cpp as", command=SaveCpp_as)
cpp_menu.add_command(label="Run Cpp", command=RunCpp)
# add commands in flie menu
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)
# add commands in edit menu
edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
run_menu.add_command(label="Run", accelerator="F5", command=run)
# function to display and hide status bar
show_status_bar = BooleanVar()
show_status_bar.set(True)
def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False 
    else :
        status_bars.pack(side=BOTTOM)
        show_status_bar = True
        
view_menu.add_checkbutton(label = "Status Bar" , onvalue = True, offvalue = 0,variable = show_status_bar , command = hide_statusbar)
# create a label for status bar
status_bars = ttk.Label(window,text = "Adipoli IDE \t\t\t\t\t\t characters: 0 words: 0")
status_bars.pack(side = BOTTOM)
# function to display count and word characters
text_change = False
def change_word(event = None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text = f"Adipoli IDE \t\t\t\t\t\t characters: {chararcter} words: {word}")
    editor.edit_modified(False)
editor.bind("<<Modified>>",change_word)
# function for light mode window
def light():
    editor.config(fg="black",bg="white")
    output_window.config(fg="black",bg="white")
# function for dark mode window
def dark():
    editor.config(fg="white", bg="black")
    output_window.config(fg="white", bg="black")
# add commands to change themes
theme_menu.add_command(label="light", command=light)
theme_menu.add_command(label="dark", command=dark)
# create output window to display output of written code
output_window = ScrolledText(window, height=10)
output_window.pack(fill=BOTH, expand=1)
window.mainloop()