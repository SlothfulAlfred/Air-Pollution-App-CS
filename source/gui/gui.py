import os
from tkinter import *
from tkinter import messagebox
from country import Country
from region import Region
from country_map_generator import region_map
from continent_map_generator import continent_map
from map_delete import map_delete
from pie_chart import create_pie_regions,create_pie_countries
import matplotlib as plt
from PIL import Image, ImageTk
import webbrowser  # Use to create footer that will link back to GitHub
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame for all menu buttons

map_delete()
root.title('Air Pollution App')

Icon_path =  "source\gui\images\\icon.png"
Icon = Image.open(Icon_path, mode="r")
Icon = ImageTk.PhotoImage(file=Icon_path, master=root)
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


footer = Button(text = "Source Code:", image = Footer, compound = LEFT, command = popup, relief=FLAT)
footer.place(width = 100, height = 30,rely = 0.9525, relx = 0.921)

GraphFrame = Frame(root)
GraphFrame.place(anchor = CENTER, relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.9)
MapFrame = Frame(root)
MapFrame.place(anchor = CENTER, relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.9)
HomeFrame = Frame(root)
HomeFrame.place(anchor = CENTER, relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.9)

# Home Button:
HomeButton = Button(root, text = "HOME", command = HomeFrame.lift, relief=FLAT)

# Map Button:
MapButton = Button(root, text = "MAP", command = MapFrame.lift, relief=FLAT)

# Graph Button
GraphButton = Button(root, text = "GRAPH", command = GraphFrame.lift, relief=FLAT)

# Canvas with Label on top of it
title_image = Canvas(HomeFrame,height = 300,width = 300)
titleimage_path =  "source\gui\images\\titleimage.png"
image = Image.open(titleimage_path, mode="r")
image = image.resize((300,300))
image = ImageTk.PhotoImage(image,master=root)
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
image2 = ImageTk.PhotoImage(image2,master=root)
map_image.create_image(150,150,image = image2,anchor = CENTER)
map_image.create_rectangle(0,0,300,300, fill = 'grey', stipple = 'gray50')
map_image.create_text(150,150, width = 300, text = "Map: View the amount of pollution in individual states/provinces.")

# If selected map frame
CountryFrame = Frame(MapFrame, width=1400, height=800)
CanadaFrame = Frame(MapFrame, width=1400, height=800)
USAFrame = Frame(MapFrame, width=1400, height=800)
#MexicoFrame = Frame(MapFrame, width=1400, height=800)

canadaMap_image = Canvas(CanadaFrame, height=500, width=700)
canadaMap_path = "source\gui\images\\placeholder.png"
imageCanadaMap = Image.open(canadaMap_path, mode='r')
imageCanadaMap = imageCanadaMap.resize((700, 500))
imageCanadaMap = ImageTk.PhotoImage(imageCanadaMap,master=root)
canadaMap_image.create_image(650, 350, image=imageCanadaMap, anchor=CENTER)

usaMap_image = Canvas(USAFrame, height=500, width=700)
usaMap_path = "source\gui\images\\placeholder.png"
imageusaMap = Image.open(usaMap_path, mode='r')
imageusaMap = imageusaMap.resize((700, 500))
imageusaMap = ImageTk.PhotoImage(imageusaMap,master=root)
usaMap_image.create_image(650, 350, image=imageusaMap, anchor=CENTER)

def click(number):
    if number == 1:
        CanadaFrame.lift()
        canada = Country(file="docs//canada.txt") #image for canada Frame generation
        region_map(canada)
        global canadaMap_path
        canadaMap_path = "source\gui\images\canada_map.png"
        global imageCanadaMap
        imageCanadaMap = Image.open(canadaMap_path, mode='r')
        imageCanadaMap = imageCanadaMap.resize((700, 500))
        imageCanadaMap = ImageTk.PhotoImage(imageCanadaMap,master=root)
        global canadaMap_image
        canadaMap_image.create_image(650, 350, image=imageCanadaMap, anchor=CENTER)
        canadaMap_image.place(height=1000, width=2000)
    elif number == 2:
        USAFrame.lift()
        usa = Country(file="docs//usa.txt") #image for canada Frame generation
        region_map(usa)
        global usaMap_path
        usaMap_path = "source\gui\images\\united states of america_map.png"
        global imageusaMap
        imageusaMap = Image.open(usaMap_path, mode='r')
        imageusaMap = imageusaMap.resize((700, 500))
        imageusaMap = ImageTk.PhotoImage(imageusaMap,master=root)
        global usaMap_image
        usaMap_image.create_image(650, 350, image=imageusaMap, anchor=CENTER)
        usaMap_image.place(height=1000, width=2000)
    #elif number == 3:
        #MexicoFrame.lift()



#Images for buttons
Canada_path = "source\\gui\\images\\canada.png"
CanadaImage = Image.open(Canada_path, mode="r")
CanadaImage = CanadaImage.resize((270,135))
CanadaImage = ImageTk.PhotoImage(CanadaImage,master=root)
USA_path =  "source\\gui\\images\\USA.png"
USAImage = Image.open(USA_path, mode="r")
USAImage = USAImage.resize((250,125))
USAImage = ImageTk.PhotoImage(USAImage,master=root)
#Mexico_path =  "source\gui\images\mexico.png"
#MexicoImage = Image.open(Mexico_path, mode="r")
#MexicoImage = MexicoImage.resize((250,125))
#MexicoImage = ImageTk.PhotoImage(MexicoImage,master=root)
Back_path =  "source\gui\images\\back.png"
BackImage = Image.open(Back_path, mode="r")
BackImage = BackImage.resize((100,100))
BackImage = ImageTk.PhotoImage(BackImage,master=root)

#Generates map buttons for each country
CanadaButton = Button(CountryFrame, compound = TOP, width = 100, height = 100,text = "Canada", image = CanadaImage, command =  lambda : click(1), relief=FLAT )
USAButton = Button(CountryFrame, compound = TOP, width = 100, height = 100, text = "USA", image = USAImage, command = lambda:  click(2), relief=FLAT )
#MexicoButton = Button(CountryFrame, compound = TOP, width = 100, height = 100,text = "Mexico", image = MexicoImage, command = lambda : click(3), relief=FLAT )

# Function for when you click the back button(map frame)
def backClick(number1):
    if number1 == 1:
        CanadaFrame.lower()
    elif number1 == 2:
        USAFrame.lower()
    #elif number1 == 3:
        #MexicoFrame.lower()


# Defining buttons for map page
BackButton1 = Button(CanadaFrame,compound  = TOP, image = BackImage, text = 'back', command = lambda : backClick(1), relief=FLAT)
BackButton2 = Button(USAFrame,compound  = TOP, image = BackImage, text = 'back',command = lambda : backClick(2), relief=FLAT)
#Backbutton3 = Button(MexicoFrame,compound  = TOP, image = BackImage,text = 'back' ,command = lambda : backClick(3), relief=FLAT)

# If selected graph frame
CountryFrameGraph = Frame(GraphFrame, width=1400, height=800)
CanadaFrameGraph = Frame(GraphFrame, width=1400, height=800)
USAFrameGraph = Frame(GraphFrame, width=1400, height=800)
#MexicoFrameGraph = Frame(GraphFrame, width=1400, height=800, bg='green')

#Generates graph of all countries

canadaGraph_image = Canvas(CanadaFrameGraph, height=500, width=700)
canadaGraph_path = "source\gui\images\\placeholder.png"
imageCanadaGraph = Image.open(canadaGraph_path, mode='r')
imageCanadaGraph = imageCanadaGraph.resize((700, 500))
imageCanadaGraph = ImageTk.PhotoImage(imageCanadaGraph,master=root)
canadaGraph_image.create_image(650, 350, image=imageCanadaGraph, anchor=CENTER)

usaGraph_image = Canvas(USAFrameGraph, height=500, width=700)
usaGraph_path = "source\gui\images\\placeholder.png"
imageusaGraph = Image.open(usaGraph_path, mode='r')
imageusaGraph = imageusaGraph.resize((700, 500))
imageusaGraph = ImageTk.PhotoImage(imageusaGraph,master=root)
usaGraph_image.create_image(650, 350, image=imageusaGraph, anchor=CENTER)

canadaGraph_image = Canvas(CanadaFrameGraph, height=500, width=700)
canadaGraph_path = "source\gui\images\\placeholder.png"
imageCanadaGraph = Image.open(canadaGraph_path, mode='r')
imageCanadaGraph = imageCanadaGraph.resize((700, 500))
imageCanadaGraph = ImageTk.PhotoImage(imageCanadaGraph,master=root)
canadaGraph_image.create_image(650, 350, image=imageCanadaGraph, anchor=CENTER)

#Function for when u click button (graph frame)
def clickGraph(number2):
    if number2 == 1:
        CanadaFrameGraph.lift()
        canada = Country(file="docs//canada.txt")  # image for canada Frame generation
        create_pie_regions(canada)
        global canadaGraph_path
        canadaGraph_path = "source\gui\images\Canada_pie.png"
        global imageCanadaGraph
        imageCanadaGraph = Image.open(canadaGraph_path, mode='r')
        imageCanadaGraph = imageCanadaGraph.resize((700, 500))
        imageCanadaGraph = ImageTk.PhotoImage(imageCanadaGraph,master=root)
        global canadaGraph_image
        canadaGraph_image.create_image(650, 350, image=imageCanadaGraph, anchor=CENTER)
        canadaGraph_image.place(height=1000, width=2000)
    elif number2 == 2:
        USAFrameGraph.lift()
        usa = Country(file="docs//usa.txt")  # image for usa Frame generation
        create_pie_regions(usa)
        global usaGraph_path
        usaGraph_path = "source\gui\images\\United States of America_pie.png"
        global imageusaGraph
        imageusaGraph = Image.open(usaGraph_path, mode='r')
        imageusaGraph = imageusaGraph.resize((700, 500))
        imageusaGraph = ImageTk.PhotoImage(imageusaGraph,master=root)
        global usaGraph_image
        usaGraph_image.create_image(650, 350, image=imageusaGraph, anchor=CENTER)
        usaGraph_image.place(height=1000, width=2000)
    #elif number2 == 3:
        #MexicoFrameGraph.lift()

#Generates graph buttons for each country
CanadaButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "Canada", image = CanadaImage, command =  lambda : clickGraph(1), relief=FLAT  )
USAButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100, text = "USA", image = USAImage, command = lambda:  clickGraph(2), relief=FLAT )
#MexicoButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "Mexico", image = MexicoImage, command = lambda : clickGraph(3), relief=FLAT  )

continent_map()
countryMap_image = Canvas(CountryFrame)
countryMap_path = "source\gui\images\\continent_map.png"
imageCountryMap = Image.open(countryMap_path, mode='r')
imageCountryMap = imageCountryMap.resize((400,300))
imageCountryMap = ImageTk.PhotoImage(imageCountryMap,master=root)
countryMap_image.create_image(200,150, image=imageCountryMap, anchor=CENTER)
countryMap_image.place(height = 300,width = 400,relx=0.35,rely=0.1)

canada = Country("docs/canada.txt")
usa = Country("docs/usa.txt")
mexico = Country("docs/mexico.txt")
create_pie_countries([canada,usa,mexico])
countryGraph_image = Canvas(CountryFrameGraph)
countryGraph_path = "source/gui/images/NA_pie.png"
imageCountryGraph = Image.open(countryGraph_path, mode='r')
imageCountryGraph = imageCountryGraph.resize((400,300))
imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph,master=root)
countryGraph_image.create_image(200,150, image=imageCountryGraph, anchor=CENTER)
countryGraph_image.place(height = 300,width = 400,relx=0.35,rely=0.1)

# Function for when you click the back button(graph frame)
def backclickGraph(number3):
    if number3 == 1:
        CanadaFrameGraph.lower()
    elif number3 == 2:
        USAFrameGraph.lower()
    #elif number3 == 3:
        #MexicoFrameGraph.lower()

# Defining all graph page buttons
BackButton1Graph = Button(CanadaFrameGraph,compound  = TOP, image = BackImage, text = 'back', command = lambda : backclickGraph(1), relief=FLAT)
BackButton2Graph = Button(USAFrameGraph,compound  = TOP, image = BackImage, text = 'back',command = lambda : backclickGraph(2), relief=FLAT)
#Backbutton3Graph = Button(MexicoFrameGraph,compound  = TOP, image = BackImage,text = 'back' ,command  = lambda : backclickGraph(3), relief=FLAT)

# Load all objects
GraphButton.place(anchor = NE, x = 1, y = 1, relx = 1, relwidth = 0.3333333333333333333333)
MapButton.place(relx = 0.3333333333333333333333,x = 1, y = 1, relwidth =0.3333333333333333333333)
HomeButton.place(anchor = NW, x = 1, y = 1, relwidth = 0.3333333333333333333333)
title_image.pack()
map_image.pack()

#placing all the map frames and defining their location(map frame)
#MexicoFrame.place(x = 0, y =0)
USAFrame.place(x = 0, y =0)
CanadaFrame.place(x = 0, y =0)

#lifting country frame so it will show first(map frame)
CountryFrame.place(x=0, y=0)
CountryFrame.lift()

#button placements(location) for (map frame)
#MexicoButton.place(relx=0.725, rely = 0.5, relwidth =0.2,relheight =0.3)
CanadaButton.place(relx = 0.12, rely = 0.5, relwidth =0.2,relheight =0.3)
USAButton.place(relx = 0.65, rely = 0.5, relwidth =0.2,relheight =0.3)
BackButton1.place(relx = 0.875, rely =0.65)
BackButton2.place(relx = 0.875, rely =0.65)
#.place(relx = 0.875, rely =0.65)

#placing all the map frames and defining their location(Graph frame)
#MexicoFrameGraph.place(x = 0, y =0)
USAFrameGraph.place(x = 0, y =0)
CanadaFrameGraph.place(x = 0, y =0)

#lifting country frame so it will show first(Graph frame)
CountryFrameGraph.place(x=0, y=0)
CountryFrameGraph.lift()

#button placements(location) for (Graph frame)
#MexicoButtonGraph.place(relx=0.725, rely = 0.5, relwidth =0.2,relheight =0.3)
CanadaButtonGraph.place(relx = 0.12, rely = 0.5, relwidth =0.2,relheight =0.3)
USAButtonGraph.place(relx = 0.65, rely = 0.5, relwidth =0.2,relheight =0.3)
BackButton1Graph.place(relx = 0.875, rely =0.65)
BackButton2Graph.place(relx = 0.875, rely =0.65)
#Backbutton3Graph.place(relx = 0.875, rely =0.65)



#adding images for the map frame


# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()
map_delete()
