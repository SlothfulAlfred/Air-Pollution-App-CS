
from tkinter import *
from PIL import Image, ImageTk
import pathlib
import webbrowser  # Use to create footer that will link back to GitHub
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame for all menu buttons
root.title('Air Pollution App')

filename = pathlib.Path(__file__).parent.absolute()
print(filename)


Icon_path = str(filename) + "\homeimages\icon.png"
Icon = Image.open(Icon_path,mode="r") # This is waaaaay too many zeroes. All you should need for this filepath is "Home Images/icon.png". You're already in the
                                                  # Air-Pollution-App-CS directory. Also please change 'Home Images' to 'models' or 'images' or anything without capitals and 
                                                  # without a space.
Icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False, Icon)

# Link opening function
def open():
    webbrowser.open("https://github.com/SlothfulAlfred/Air-Pollution-App-CS")

# Footer
Footer_path = str(filename) + "\homeimages\icon.png"
Footer = Image.open(Footer_path, mode="r")
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
titleimage_path = str(filename) + "\homeimages/titleimage.png"
image = Image.open(titleimage_path, mode="r")
image = image.resize((300,300))
image = ImageTk.PhotoImage(image)
title_image.create_image(150,150,image = image,anchor = CENTER)
title_image.create_rectangle(0,0,300,300, fill = 'grey', stipple = 'gray50')
title_image.create_text(150,150,width = 300, text = "HELLOTHERE1")

# Description of program
description = Label(text = "Insert text here")

# Map Canvas with label on top of it
map_image = Canvas(HomeFrame,height = 300,width = 300)
mapimage_path = str(filename) + '\homeimages\mapimage.jpg'
image2 = Image.open(mapimage_path, mode="r")
image2 = image2.resize((300,300))
image2 = ImageTk.PhotoImage(image2)
map_image.create_image(150,150,image = image2,anchor = CENTER)
map_image.create_rectangle(0,0,300,300, fill = 'grey', stipple = 'gray50')
map_image.create_text(150,150, width = 300, text = "Map: View the amount of pollution in individual states/provinces.")

#if selected map frame
CountryFrame = Frame(MapFrame, width=1400, height=800, bg = 'purple')
CanadaFrame = Frame(MapFrame, width=500, height=500, bg = 'red')
USAFrame = Frame(MapFrame, width=500, height=500, bg = 'brown')
MexicoFrame = Frame(MapFrame, width=500, height=500, bg='aqua')

def click():

    if number == 1:
        CountryFrame.lower
        CanadaFrame.lift()
    elif number == 2:
        CountryFrame.lower       
        USAFrame.lift()
    elif number == 3:
        CountryFrame.lower
        MexicoFrame.lift()



CanadaButton = Button(CountryFrame, text = "Canada image here" , command = click(1) )
USAButton = Button(CountryFrame, text = "USA image here"  , command = click(2))
MexicoButton = Button(CountryFrame, text = "Mexico image here", command = click(3))


# Load all objects

GraphButton.place(anchor = NE, x = 1, y = 1, relx = 1, relwidth = 0.3333333333333333333333)
MapButton.place(relx = 0.3333333333333333333333,x = 1, y = 1, relwidth =0.3333333333333333333333)
HomeButton.place(anchor = NW, x = 1, y = 1, relwidth = 0.3333333333333333333333)
title_image.pack()
map_image.pack()

#placing all the frames and defining their size
MexicoFrame.place(x = 0, y =0)
USAFrame.place(x = 0, y =0)
CanadaFrame.place(x = 0, y =0)

#placed last so it will show first
CountryFrame.place(x=0, y=0)
CountryFrame.lift()


#button placements
MexicoButton.place(x=400, y =30)
CanadaButton.place(x=100, y =30)
USAButton.place(x=250, y =30)
# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()

