import os
from tkinter import *
from tkinter import messagebox
from country import Country
from region import Region
from country_map_generator import region_map
from continent_map_generator import continent_map
from map_delete import map_delete
from pie_chart import create_pie_regions,create_pie_countries
from bar_chart import create_bar_countries,create_bar_regions
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
    result = messagebox.askyesno(title="Redirect Warning", message="This link directs you to the source code for this project. Click YES to proceed to our github or NO to close this message.")
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
#NA_Frame = Frame(MapFrame, width=1400, height=800)

continent_map()
countryMap_image = Canvas(CountryFrame)
countryMap_path = "source\gui\images\\continent_map.png"
imageCountryMap = Image.open(countryMap_path, mode='r')
imageCountryMap = imageCountryMap.resize((400,300))
imageCountryMap = ImageTk.PhotoImage(imageCountryMap,master=root)
countryMap_image.create_image(650, 350, image=imageCountryMap, anchor=CENTER)
countryMap_image.place(height=1000, width=2000, relx=0.05, rely=-0.15)

def click(number):
    global countryMap_path
    global imageCountryMap
    global countryMap_image
    if number == 1:
        canada = Country(file="docs//canada.txt") #image for canada Frame generation
        region_map(canada)
        countryMap_path = "source\gui\images\canada_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((400, 300))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap,master=root)
        countryMap_image.create_image(650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(height=1000, width=2000, relx=0.05, rely=-0.15)
    elif number == 2:
        usa = Country(file="docs//usa.txt") #image for canada Frame generation
        region_map(usa)
        countryMap_path = "source\gui\images\\united states of america_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((400, 300))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(height=1000, width=2000, relx=0.05, rely=-0.15)
    elif number == 3:
        continent_map()
        countryMap_path = "source\gui\images\\continent_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((400, 300))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(height=1000, width=2000, relx=0.05, rely=-0.15)



#Images for buttons
Canada_path = "source\\gui\\images\\canada.png"
CanadaImage = Image.open(Canada_path, mode="r")
CanadaImage = CanadaImage.resize((270,135))
CanadaImage = ImageTk.PhotoImage(CanadaImage,master=root)
USA_path =  "source\\gui\\images\\USA.png"
USAImage = Image.open(USA_path, mode="r")
USAImage = USAImage.resize((250,125))
USAImage = ImageTk.PhotoImage(USAImage,master=root)
NA_path =  "source\gui\images\\NA.png"
NA_Image = Image.open(NA_path, mode="r")
NA_Image = NA_Image.resize((250,125))
NA_Image = ImageTk.PhotoImage(NA_Image,master=root)
Back_path =  "source\gui\images\\back.png"
BackImage = Image.open(Back_path, mode="r")
BackImage = BackImage.resize((100,100))
BackImage = ImageTk.PhotoImage(BackImage,master=root)

#Generates map buttons for each country
CanadaButton = Button(CountryFrame, compound = TOP, width = 100, height = 100,text = "Canada", image = CanadaImage, command =  lambda : click(1), relief=FLAT )
USAButton = Button(CountryFrame, compound = TOP, width = 100, height = 100, text = "USA", image = USAImage, command = lambda:  click(2), relief=FLAT )
NA_Button = Button(CountryFrame, compound = TOP, width = 100, height = 100,text = "North America", image = NA_Image, command = lambda : click(3), relief=FLAT )

# Function for when you click the back button(map frame)
def backClick(number1):
    if number1 == 1:
        CanadaFrame.lower()
    elif number1 == 2:
        USAFrame.lower()
    #elif number1 == 3:
        #NA_Frame.lower()

# If selected graph frame
CountryFrameGraph = Frame(GraphFrame, width=1400, height=800)
CanadaFrameGraph = Frame(GraphFrame, width=1400, height=800)
USAFrameGraph = Frame(GraphFrame, width=1400, height=800)
#NA_FrameGraph = Frame(GraphFrame, width=1400, height=800, bg='green')

#Generates graph of all countries

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

create_bar = False

#Function for when u click button (graph frame)
def clickGraph(number2):
    global countryGraph_path
    global imageCountryGraph
    global countryGraph_image
    global create_bar
    if number2 == 1:
        canada = Country(file="docs//canada.txt")  # image for canada Frame generation
        if create_bar == True:
            create_bar_regions(canada)
            countryGraph_path = "source\gui\images\Canada_bar.png"
        else:
            create_pie_regions(canada)
            countryGraph_path = "source\gui\images\Canada_pie.png"
        imageCountryGraph = Image.open(countryGraph_path, mode='r')
        imageCountryGraph = imageCountryGraph.resize((400,300))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph,master=root)
        countryGraph_image.create_image(200,150, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(height = 300,width = 400,relx=0.35,rely=0.1)
    elif number2 == 2:
        usa = Country(file="docs//usa.txt")  # image for usa Frame generation
        create_pie_regions(usa)
        countryGraph_path = "source\gui\images\\United States of America_pie.png"
        if create_bar == True:
            create_bar_regions(usa)
            countryGraph_path = "source\gui\images\\United States of America_bar.png"
        else:
            create_pie_regions(usa)
            countryGraph_path = "source\gui\images\\United States of America_pie.png"
        imageCountryGraph = Image.open(countryGraph_path, mode='r')
        imageCountryGraph = imageCountryGraph.resize((400, 300))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(200, 150, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(height=300, width=400, relx=0.35, rely=0.1)
    elif number2 == 3:
        canada = Country("docs/canada.txt")
        usa = Country("docs/usa.txt")
        mexico = Country("docs/mexico.txt")
        if create_bar == True:
            create_bar_countries([canada, usa, mexico])
            countryGraph_path = "source/gui/images/NA_bar.png"
        else:
            create_pie_countries([canada, usa, mexico])
            countryGraph_path = "source/gui/images/NA_pie.png"
        imageCountryGraph = Image.open(countryGraph_path, mode='r')
        imageCountryGraph = imageCountryGraph.resize((400, 300))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(200, 150, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(height=300, width=400, relx=0.35, rely=0.1)

def graph_switch():
    global create_bar
    create_bar = not create_bar

GraphToggle = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "Switch Graph Types", command =  lambda : graph_switch(), relief=FLAT)

#Generates graph buttons for each country
CanadaButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "Canada", image = CanadaImage, command =  lambda : clickGraph(1), relief=FLAT  )
USAButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100, text = "USA", image = USAImage, command = lambda:  clickGraph(2), relief=FLAT )
NA_ButtonGraph = Button(CountryFrameGraph, compound = TOP, width = 100, height = 100,text = "North America", image = NA_Image, command = lambda : clickGraph(3), relief=FLAT  )

# Load all objects
GraphButton.place(anchor = NE, x = 1, y = 1, relx = 1, relwidth = 0.3333333333333333333333)
MapButton.place(relx = 0.3333333333333333333333,x = 1, y = 1, relwidth =0.3333333333333333333333)
HomeButton.place(anchor = NW, x = 1, y = 1, relwidth = 0.3333333333333333333333)
title_image.pack()
map_image.pack()

#lifting country frame so it will show first(map frame)
CountryFrame.place(x=0, y=0)
CountryFrame.lift()

#button placements(location) for (map frame)
NA_Button.place(relx=0.725, rely = 0.5, relwidth =0.2,relheight =0.3)
CanadaButton.place(relx = 0.055, rely = 0.5, relwidth =0.2,relheight =0.3)
USAButton.place(relx = 0.39, rely = 0.5, relwidth =0.2,relheight =0.3)

#lifting country frame so it will show first(Graph frame)
CountryFrameGraph.place(x=0, y=0)
CountryFrameGraph.lift()

#button placements(location) for (Graph frame)
NA_ButtonGraph.place(relx=0.725, rely = 0.5, relwidth =0.2,relheight =0.3)
CanadaButtonGraph.place(relx = 0.055, rely = 0.5, relwidth =0.2,relheight =0.3)
GraphToggle.place(relx = 0.055, rely = 0.3, relwidth =0.2,relheight =0.3)
USAButtonGraph.place(relx = 0.39, rely = 0.5, relwidth =0.2,relheight =0.3)

# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()
map_delete()
