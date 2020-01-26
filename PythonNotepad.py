# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI SCRIPT FOR A SIMPLE NOTEPAD APPLICATION USING tkinter MODULE

# Importing necessary packages
import tkinter as tk
from tkinter import *
from datetime import datetime as dt
from tkinter import filedialog, messagebox

# Defining CreateWidgets() function to create necessary tkinter widgets
# FOR BUTTON BACKGROUND COLOR USE bg ARGUMENT IN WINDOWS AND highlightbackground ARGUMENT IN MAC
def CreateWidgets():
    saveFileLabel = Label(root, text='FILE NAME : ', font=('', 15, 'bold'), bg='steelblue')
    saveFileLabel.grid(row=0, column=0, padx=5, pady=5)

    saveFileEntry = Entry(root, width=50, textvariable=fileName, bg='darkgrey')
    saveFileEntry.grid(row=0, column=1, padx=5, pady=5)

    fileBrowseButton = Button(root, text='BROWSE', width=20, command=fileBrowse, highlightbackground='yellow')
    fileBrowseButton.grid(row=0, column=2, padx=5, pady=5)

    fileTextLabel = Label(root, text='FILE TEXT : ', font=('', 15, 'bold'), bg='steelblue')
    fileTextLabel.grid(row=1, column=0, padx=5, pady=5)

    root.fileTextEntry = Text(root, width=120, height=30, bg='darkgrey')
    root.fileTextEntry.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    clearTextButton = Button(root, text='CLEAR TEXT', width=20, command=textClear, highlightbackground='red')
    clearTextButton.grid(row=3, column=0, padx=5, pady=5)

    fileSaveButton = Button(root, text='SAVE TEXT', width=20, command=fileWrite, highlightbackground='green')
    fileSaveButton.grid(row=3, column=2, padx=5, pady=5)

# Defining the Browse() to save the file
def fileBrowse():
    # Fetching the user-input filename and destination path using asksaveasfilename
    # Setting the initialdir and filetypes arguments are option
    f_name = filedialog.asksaveasfilename(initialdir='YOUR DESTINATION PATH',
                                          filetypes=(('Text File (*.txt)','*.txt'),
                                                     ('DOC File (*.doc)','*.doc'),
                                                     ('All File')))
    # Setting the fileName tkinter variable to the file_name value
    fileName.set(f_name)

# Defining the textClear() to clear the contents of the fileTextEntry
def textClear():
    # Clearing the contents of the fileTextEntry using the delete()
    root.fileTextEntry.delete('1.0', END)

# Defining the fileWrite() to write the contents of fileTextEntry to either the user-specifed file or default file
def fileWrite():
    # Getting the filename with the path using the get() and storing it in the file_name_path
    file_name_path = fileName.get()
        # Checking if the user has entered file name and destination
    if len(file_name_path) != 0:
        # Opening the file in write mode with fileOpen as the file object
        with open(file_name_path, 'w') as fileOpen:
            # Getting the contents of the fileTextEntry using the get() and storing in fileContent
            fileContent = root.fileTextEntry.get('1.0', END)
            # Writing the fileContent to the file using write()
            fileOpen.write(fileContent)
            # Displaying message
            messagebox.showinfo('SUCCESS!','FILE SAVED')

    # If the user has not entered the file name and path, saving the file in default location with the current date
    # and time as the file name
    else:
        default_path = 'DEFAULT DESTINATION PATH OF YOUR CHOICE TO SAVE FILES'
        default_filename = default_path + str(dt.now().strftime('%d%m%Y %H%M'))+'.txt'
        # Opening the file in write mode with fileOpen as the file object
        with open(default_filename, 'w') as fileOpen:
            # Getting the contents of the fileTextEntry using the get() and storing in fileContent
            fileContent = root.fileTextEntry.get('1.0', END)
            # Writing the fileContent to the file using write()
            fileOpen.write(fileContent)
            # Displaying message
            messagebox.showinfo('SUCCESS!', 'FILE SAVED')

# Creating object root of tk
root = tk.Tk()

# Setting the title, window size, background color and disabling the resizing property
root.title('PyNotepad')
root.geometry('860x560')
root.resizable(False, False)
root.configure(background='steelblue')

# Creating tkinter variable
fileName = StringVar()

CreateWidgets()

# Defining infinite loop to run application
root.mainloop()