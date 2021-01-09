from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import pathlib
import webbrowser  # Use to create footer that will link back to GitHub
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame for all menu buttons
root.title('Air Pollution App')


Icon_path =  "source\gui\images\icon.png"
Icon = Image.open(Icon_path, mode="r") 

Icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False, Icon)


    

# Footer
Footer_path =  "source\gui\images\\footer.png"
Footer = Image.open(Footer_path, mode="r")
Footer = Footer.resize((19,19))
Footer = ImageTk.PhotoImage(Footer)
# Link opening function

def popup():
    result = tk.messagebox.askyesno(title="Redirect Warning", message="This link directs you to the source code for this project. Click YES to proceed to our github or NO to close this message.")
    if result == True:
       webbrowser.open("https://github.com/SlothfulAlfred/Air-Pollution-App-CS")
    


footer = Button(text = "Source Code:", image = Footer, compound = LEFT, command = popup)
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

# Canvas with Label on top of it
title_image = Canvas(HomeFrame,height = 300,width = 300)
titleimage_path =  "source\gui\images\\titleimage.png"
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
mapimage_path =  'source\gui\images\mapimage.jpg'
image2 = Image.open(mapimage_path, mode="r")
image2 = image2.resize((300,300))
image2 = ImageTk.PhotoImage(image2)
map_image.create_image(150,150,image = image2,anchor = CENTER)
map_image.create_rectangle(0,0,300,300, fill = 'grey', stipple = 'gray50')
map_image.create_text(150,150, width = 300, text = "Map: View the amount of pollution in individual states/provinces.")

# If selected map frame
CountryFrame = Frame(MapFrame, width=1400, height=800, bg = 'purple')
CanadaFrame = Frame(MapFrame, width=1400, height=800, bg = 'red')
USAFrame = Frame(MapFrame, width=1400, height=800, bg = 'brown')
MexicoFrame = Frame(MapFrame, width=1400, height=800, bg='aqua')

#image for canada Frame
canadaMap_image = Canvas(CanadaFrame,height = 500,width = 700)
canadaMap_path =  "source\gui\images\\canada_map.png"
imageCanadaMap = Image.open(canadaMap_path, mode= 'r')
imageCanadaMap = imageCanadaMap.resize((700,500))
imageCanadaMap = ImageTk.PhotoImage(imageCanadaMap)
canadaMap_image.create_image(650,350, image = imageCanadaMap,anchor = CENTER)
canadaMap_image.place(height=1000, width =2000)



# Function for when u click button (map frame)

def click(number):
    if number == 1:
        CanadaFrame.lift()
    elif number == 2:
        USAFrame.lift()
    elif number == 3:
        MexicoFrame.lift()

# Images for buttons
Canada_path =  "\\source\\gui\\images\\canada.png"
CanadaImage = Image.open(Canada_path, mode="r")
CanadaImage = CanadaImage.resize((270,135))
CanadaImage = ImageTk.PhotoImage(CanadaImage)
USA_path =  "\\source\\gui\\images\\USA.png"
USAImage = Image.open(USA_path, mode="r")
USAImage = USAImage.resize((250,125))
USAImage = ImageTk.PhotoImage(USAImage)
Mexico_path =  "\source\gui\images\mexico.png"
MexicoImage = Image.open(Mexico_path, mode="r")
MexicoImage = MexicoImage.resize((250,125))
MexicoImage = ImageTk.PhotoImage(MexicoImage)
Back_path =  "\source\gui\images\back.png"
BackImage = Image.open(Back_path, mode="r")
BackImage = BackImage.resize((100,100))
BackImage = ImageTk.PhotoImage(BackImage)

CanadaButton = Button(CountryFrame, compound = TOP, width = 100, height = 100,text = "Canada", image = CanadaImage, command =  lambda : click(1) )
USAButton = Button(CountryFrame, compound = TOP, width = 100, height = 100, text = "USA", image = USAImage, command = lambda:  click(2) )
MexicoButton = Button(CountryFrame, compound = TOP, width = 100, height = 100,text = "Mexico", image = MexicoImage, command = lambda : click(3) )

# Function for when you click the back button(map frame)
def backClick(number1):
    if number1 == 1:
        CanadaFrame.lower() 
    elif number1 == 2:
        USAFrame.lower()
    elif number1 == 3:
        MexicoFrame.lower()


# Defining buttons for map page
BackButton1 = Button(CanadaFrame,compound  = TOP, image = BackImage, text = 'back', command = lambda : backClick(1))
BackButton2 = Button(USAFrame,compound  = TOP, image = BackImage, text = 'back',command = lambda : backClick(2))
Backbutton3 = Button(MexicoFrame,compound  = TOP, image = BackImage,text = 'back' ,command = lambda : backClick(3))

# If selected graph frame
CountryFrameGraph = Frame(GraphFrame, width=1400, height=800, bg = 'pink')
CanadaFrameGraph = Frame(GraphFrame, width=1400, height=800, bg = 'beige')
USAFrameGraph = Frame(GraphFrame, width=1400, height=800, bg = 'blue')
MexicoFrameGraph = Frame(GraphFrame, width=1400, height=800, bg='green')





#Function for when u click button (graph frame)
def clickGraph(number2):
    if number2 == 1:
        CanadaFrameGraph.lift() 
    elif number2 == 2:
        USAFrameGraph.lift()
    elif number2 == 3:
        MexicoFrameGraph.lift()

CanadaButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "Canada", image = CanadaImage, command =  lambda : clickGraph(1)  )
USAButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100, text = "USA", image = USAImage, command = lambda:  clickGraph(2) )
MexicoButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "Mexico", image = MexicoImage, command = lambda : clickGraph(3)  )

# Function for when you click the back button(graph frame)
def backclickGraph(number3):
    if number3 == 1:
        CanadaFrameGraph.lower() 
    elif number3 == 2:
        USAFrameGraph.lower()
    elif number3 == 3:
        MexicoFrameGraph.lower()   

# Defining all graph page buttons
BackButton1Graph = Button(CanadaFrameGraph,compound  = TOP, image = BackImage, text = 'back', command = lambda : backclickGraph(1))
BackButton2Graph = Button(USAFrameGraph,compound  = TOP, image = BackImage, text = 'back',command = lambda : backclickGraph(2))
Backbutton3Graph = Button(MexicoFrameGraph,compound  = TOP, image = BackImage,text = 'back' ,command  = lambda : backclickGraph(3))

# Load all objects
GraphButton.place(anchor = NE, x = 1, y = 1, relx = 1, relwidth = 0.3333333333333333333333)
MapButton.place(relx = 0.3333333333333333333333,x = 1, y = 1, relwidth =0.3333333333333333333333)
HomeButton.place(anchor = NW, x = 1, y = 1, relwidth = 0.3333333333333333333333)
title_image.pack()
map_image.pack()

#placing all the map frames and defining their location(map frame)
MexicoFrame.place(x = 0, y =0)
USAFrame.place(x = 0, y =0)
CanadaFrame.place(x = 0, y =0)

#lifting country frame so it will show first(map frame)
CountryFrame.place(x=0, y=0)
CountryFrame.lift()

#button placements(location) for (map frame)
MexicoButton.place(relx=0.725, rely = 0.35, relwidth =0.2,relheight =0.3)
CanadaButton.place(relx = 0.055, rely = 0.35, relwidth =0.2,relheight =0.3)
USAButton.place(relx = 0.39, rely = 0.35, relwidth =0.2,relheight =0.3)
BackButton1.place(relx = 0.875, rely =0.65)
BackButton2.place(relx = 0.875, rely =0.65)
Backbutton3.place(relx = 0.875, rely =0.65)

#placing all the map frames and defining their location(Graph frame)
MexicoFrameGraph.place(x = 0, y =0)
USAFrameGraph.place(x = 0, y =0)
CanadaFrameGraph.place(x = 0, y =0)

#lifting country frame so it will show first(Graph frame)
CountryFrameGraph.place(x=0, y=0)
CountryFrameGraph.lift()

#button placements(location) for (Graph frame)
MexicoButtonGraph.place(relx=0.725, rely = 0.35, relwidth =0.2,relheight =0.3)
CanadaButtonGraph.place(relx = 0.055, rely = 0.35, relwidth =0.2,relheight =0.3)
USAButtonGraph.place(relx = 0.39, rely = 0.35, relwidth =0.2,relheight =0.3)
BackButton1Graph.place(relx = 0.875, rely =0.65)
BackButton2Graph.place(relx = 0.875, rely =0.65)
Backbutton3Graph.place(relx = 0.875, rely =0.65)



#adding images for the map frame


# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()
