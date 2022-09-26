from tkinter import *
import tkinter

root = Tk()
root.title("Download Image")  

searchText = StringVar()
def click():
    print(searchText.get())

# Creating search part
searchLabel = Label(root, text = "Search Image Name: ").grid(row = 0, column= 0, sticky="w")

searchEntry = Entry(root, width= 30, textvariable= searchText).grid(row=0, column= 1, padx= 2, pady= 2, sticky= "we", columnspan=9)
searchButton = Button(root, text= "Search", command = click).grid(row= 1, column=9, sticky= "we" )


root.mainloop()

