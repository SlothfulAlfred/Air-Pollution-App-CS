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
CanadaFrame = Frame(MapFrame, width=1400, height=800, bg = 'red')
USAFrame = Frame(MapFrame, width=1400, height=800, bg = 'brown')
MexicoFrame = Frame(MapFrame, width=1400, height=800, bg='aqua')
#function for when u click button (map frame)

def canadaClick():
    CanadaFrame.lift() 
def usaClick():
    USAFrame.lift()
def mexicoClick():
    MexicoFrame.lift()   



CanadaButton = Button(CountryFrame, text = "Canada image here" , command = canadaClick )
USAButton = Button(CountryFrame, text = "USA image here"  , command =usaClick )
MexicoButton = Button(CountryFrame, text = "Mexico image here", command =mexicoClick )
#function for when you click the back button(graph frame)

def backCanada():
    CanadaFrame.lower() 
    

def backUSA():
    USAFrame.lower()
   

def backMexico():
    MexicoFrame.lower()   
    


BackButton1 = Button(CanadaFrame, text = 'back', command = backCanada)
BackButton2 = Button(USAFrame, text = 'back',command = backUSA)
Backbutton3 = Button(MexicoFrame,text = 'back' ,command = backMexico)





#if selected graph frame
CountryFrameGraph = Frame(GraphFrame, width=1400, height=800, bg = 'pink')
CanadaFrameGraph = Frame(GraphFrame, width=1400, height=800, bg = 'beige')
USAFrameGraph = Frame(GraphFrame, width=1400, height=800, bg = 'blue')
MexicoFrameGraph = Frame(GraphFrame, width=1400, height=800, bg='green')
#function for when u click button (graph frame)
def canadaClickGraph():
    CanadaFrameGraph.lift() 
def usaClickGraph():
    USAFrameGraph.lift()
def mexicoClickGraph():
    MexicoFrameGraph.lift()   



CanadaButtonGraph = Button(CountryFrameGraph, text = "Canada image here" , command = canadaClickGraph )
USAButtonGraph = Button(CountryFrameGraph, text = "USA image here"  , command =usaClickGraph )
MexicoButtonGraph = Button(CountryFrameGraph, text = "Mexico image here", command =mexicoClickGraph )
#function for when you click the back button(graph frame)
def backCanadaGraph():
    CanadaFrameGraph.lower() 
def backUSAGraph():
    USAFrameGraph.lower()
def backMexicoGraph():
    MexicoFrameGraph.lower()   
    


BackButton1Graph = Button(CanadaFrameGraph, text = 'back', command = backCanadaGraph)
BackButton2Graph = Button(USAFrameGraph, text = 'back',command = backUSAGraph)
Backbutton3Graph = Button(MexicoFrameGraph,text = 'back' ,command = backMexicoGraph)

















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
MexicoButton.place(x=1200, y =300)
CanadaButton.place(x=300, y =300)
USAButton.place(x=700, y =300)
BackButton1.place(x = 1000, y=600)
BackButton2.place(x = 1000, y=600)
Backbutton3.place(x = 1000, y=600)

#placing all the map frames and defining their location(Graph frame)
MexicoFrameGraph.place(x = 0, y =0)
USAFrameGraph.place(x = 0, y =0)
CanadaFrameGraph.place(x = 0, y =0)

#lifting country frame so it will show first(Graph frame)
CountryFrameGraph.place(x=0, y=0)
CountryFrameGraph.lift()

#button placements(location) for (Graph frame)
MexicoButtonGraph.place(x=1200, y =300)
CanadaButtonGraph.place(x=300, y =300)
USAButtonGraph.place(x=700, y =300)
BackButton1Graph.place(x = 1000, y=600)
BackButton2Graph.place(x = 1000, y=600)
Backbutton3Graph.place(x = 1000, y=600)




# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()


