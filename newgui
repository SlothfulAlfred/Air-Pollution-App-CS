# AFAIK the Image class from PIL only supports some obscure file types and doesn't support .png or .jpg
# you need to do ImageTk.PhotoImage(Image.open('filename.whatever')) for it to work with .png
# also you need to fix the image pathways. putting a '.' in the file path takes you up one level and '/' or '\' takes you 
# down one level. ex. if you want the file toad.png with filepath "source/gui/models/toad.png", and the current file is 
# in "source/gui/code/page1.py" then the filepath should be "../models/toad.png". which is the same as 
# "gui/models/toad.png". Putting the whole filepath like C:/Users/.../whatever.whatever is not going to work on any
# computer other than your own. Conversly, putting ../folder/folder2/whatever.whatever will work on any computer 
# including yours.

from tkinter import *
from PIL import Image, ImageTk
import webbrowser  # Use to create footer that will link back to GitHub
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame for all menu buttons
root.title('Air Pollution App')

Icon = Image.open(r"./Home Images/icon.png")
Icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False, Icon)

# Link opening function
def open():
    webbrowser.open("https://github.com/SlothfulAlfred/Air-Pollution-App-CS")

# Footer
Footer = Image.open(r"./Home Images/footer.png")
Footer = Footer.resize((19,19))
Footer = ImageTk.PhotoImage(Footer)

footer = Button(text = "Source Code:", command = open, image = Footer, compound = LEFT)
footer.place(width = 100, height = 30,rely = 0.9525, relx = 0.921)

GraphFrame = Frame(root, bg = 'green')
GraphFrame.place(anchor = CENTER, relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.9)
MapFrame = Frame(root, bg = 'blue')
MapFrame.place(anchor = CENTER, relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.9)
HomeFrame = Frame(root, bg = 'red')
HomeFrame.place(anchor = CENTER, relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.9)

# Home Button:
HomeButton = Button(root, text = "HOME", command = HomeFrame.lift)
# Map Button:
MapButton = Button(root, text = "MAP", command = MapFrame.lift)
# Graph Button
GraphButton = Button(root, text = "GRAPH", command = GraphFrame.lift)


# Home frame

# Canvas with Label on top of it
title_image = Canvas(HomeFrame,height = 300,width = 300)
image = Image.open(r"./Home Images/titleimage.png")
image = image.resize((300,300))
image = ImageTk.PhotoImage(image)
title_image.create_image(150,150,image = image,anchor = CENTER)
title_image.create_rectangle(0,0,300,300, fill = 'grey', stipple = 'gray50')
title_image.create_text(150,150,width = 300, text = "HELLOTHERE1")

# Description of program
description = Label(text = "Insert text here")

# Map Canvas with label on top of it
map_image = Canvas(HomeFrame,height = 300,width = 300)
image2 = Image.open(r"./Home Images/mapimage.jpg")
image2 = image2.resize((300,300))
image2 = ImageTk.PhotoImage(image2)
map_image.create_image(150,150,image = image2,anchor = CENTER)
map_image.create_rectangle(0,0,300,300, fill = 'grey', stipple = 'gray50')
map_image.create_text(150,150, width = 300, text = "Map: View the amount of pollution in individual states/provinces.")

# Load all objects

GraphButton.place(anchor = NE, x = 1, y = 1, relx = 1, relwidth = 0.3333333333333333333333)
MapButton.place(relx = 0.3333333333333333333333,x = 1, y = 1, relwidth =0.3333333333333333333333)
HomeButton.place(anchor = NW, x = 1, y = 1, relwidth = 0.3333333333333333333333)
title_image.pack()
map_image.pack()

# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()
