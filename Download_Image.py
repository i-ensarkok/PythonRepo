from tkinter import *
from bing_image_downloader import downloader


# Main window specifications
root = Tk()
root.geometry("500x240")
root.title("Download Image")
root.resizable(0,0)  

# Variables
searchText = StringVar()
numImgText = StringVar()
outputDirText = StringVar()

def download():
    downloader.download(searchText.get(), limit= int(numImgText.get()), output_dir= outputDirText.get(), 
    adult_filter_off=True, force_replace= False, timeout=60, verbose=True)


def click():
    if len(searchText.get()) != 0 :
        print(searchText.get())
        download()
    else:
        print("Entry is null")

# Creating search block
searchLabel = Label(root, text = "Search Image Name: ").grid(row = 0, column= 0, sticky="w")
searchEntry = Entry(root, width= 30, textvariable= searchText).grid(row=0, column= 1, padx= 2, pady= 2, sticky= "w", columnspan=9)
searchButton = Button(root, text= "Search", command = click).grid(row= 3, column=9, sticky= "w" )

# Creating image block
numImgLabel = Label(root, text= "Number of images to download: ").grid(row= 1, column= 0, sticky= "w")
numImgEntry = Entry(root, width= 10, textvariable= numImgText).grid(row= 1, column= 1, padx= 2, pady= 2, sticky="w") 

# Creating output direction block
outputDirLabel = Label(root, text= "Output direction folder name: ").grid(row= 2, column= 0, sticky= "w")
outputDirEntry = Entry(root, width= 15, textvariable= outputDirText).grid(row= 2, column= 1, padx= 2, pady= 2, sticky="w") 
root.mainloop()

