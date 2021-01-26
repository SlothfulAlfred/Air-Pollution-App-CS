# -----------------------------------------------------
# Name:             Air Pollution App (main.py)
# Purpose:          To create an app to raise awareness about climate change and air pollution in North America
#
#
#
# Author:           Alfred Mikhael, 627582
# Created:          27-Sep-2020
# Updated:          4-Dec-2020
# References:       All coordinate data is taken from https://www.latlong.net/category/states-236-14.html.
#                   Greenhouse gas statistics are taken from Stats Canada or US Energy Information Administration
#                   for Canadian and American values respectively.
# ----------------------------------------------------
import os
from tkinter import *
from tkinter import messagebox
from source.helpers.country import Country
from source.helpers.region import Region
from source.helpers.country_map_generator import region_map
from source.helpers.continent_map_generator import continent_map
from source.helpers.deletion import mapDelete, graphDelete
from source.helpers.pie_chart import create_pie_regions, create_pie_countries
from source.helpers.bar_chart import create_bar_countries, create_bar_regions
import plotly.express as px
import matplotlib as plt
from PIL import Image, ImageTk
import webbrowser  # Use to create footer that will link back to GitHub

# Initializes window
root = Tk()
height_px = root.winfo_screenheight()
width_px = root.winfo_screenwidth()
print(width_px)
print(height_px)


# Initialize Country objects used for maps and graphs
canada = Country("docs/canada.txt")
usa = Country("docs/usa.txt")
mexico = Country("docs/mexico.txt")

# Clears any pre-generated maps
mapDelete('source/images/')
graphDelete('source/images/')
create_bar = True

# Initializing of title and icon image
root.title('Air Pollution App')
Icon_path = r"source\images\\icon.png"
Icon = Image.open(Icon_path, mode="r")
Icon = ImageTk.PhotoImage(file=Icon_path, master=root)
root.iconphoto(False, Icon)

# Footer which links to Source Code
Footer_path = r"source\images\\footer.png"
Footer = Image.open(Footer_path, mode="r")
Footer = Footer.resize((19, 19))
Footer = ImageTk.PhotoImage(Footer)

def popup():
    '''
    Displays a popup window, and if the user wishes to takes them to the project's source code
    '''
    result = messagebox.askyesno(
        title="Redirect Warning",
        message="This link directs you to the source code for this project. Click YES to proceed to our github or NO to close this message.")
    if result:
        webbrowser.open(
            "https://github.com/SlothfulAlfred/Air-Pollution-App-CS")


footer = Button(
    text="Source Code:",
    image=Footer,
    compound=LEFT,
    command=popup,
    relief=FLAT)
footer.place(relwidth=0.08, relheight=0.0277777777777778, rely=0.9525, relx=0.921)

# Generating Home, Map and Graph pages
GraphFrame = Frame(root)
GraphFrame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=0.9)
MapFrame = Frame(root)
MapFrame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=0.9)
HomeFrame = Frame(root)
HomeFrame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=0.9)

# Creating menu buttons
HomeButton = Button(root, text="HOME", command=HomeFrame.lift, relief=FLAT)
MapButton = Button(root, text="MAP", command=MapFrame.lift, relief=FLAT)
GraphButton = Button(root, text="GRAPH", command=GraphFrame.lift, relief=FLAT)

# Creation of Home Page images + text
title_image = Canvas(HomeFrame, height=300*(height_px/864), width=width_px)
titleimage_path = r"source\images\\titleimage.png"
image = Image.open(titleimage_path, mode="r")
image = image.resize((int(width_px*1.25),300))
image = ImageTk.PhotoImage(image, master=root)
title_image.create_image(600*(width_px/1536),150*(height_px/864), image=image)
title_image.create_rectangle(0, 0, width_px, 300*(height_px/864), fill='grey', stipple='gray50')
title_image.create_text(805*(width_px/1536), 150*(height_px/864), width=width_px, text="In the modern day, keeping countries accountable for the CO2 emissions "
   "is becoming increasingly difficult.\n"
   "The main reason for this is that there are very few ways for the general public to understand the scope "
   "of their emissions. \n We aim to change that."
                        , font=("Helvetica",14))

description = Label(text="Insert text here")
map_image = Canvas(HomeFrame, height=300, width=300)
mapimage_path = r'source\images\mapimage.jpg'
image2 = Image.open(mapimage_path, mode="r")
image2 = image2.resize((300, 300))
image2 = ImageTk.PhotoImage(image2, master=root)
map_image.create_image(150, 150, image=image2, anchor=CENTER)
map_image.create_rectangle(0, 0, 300, 300, fill='grey', stipple='gray50')
map_image.create_text(
    150,
    150,
    width=300,
    text="With the aim of reducing the effects of climate change, our application will provide statistical and visual methods of understanding the impact of some of the world's largest countries on Earth's climate, based on data from reputable sources. ")


# Map Page Initialization
continent_map()
countryMap_image = Canvas(MapFrame)
countryMap_path = r"source\images\\continent_map.png"
imageCountryMap = Image.open(countryMap_path, mode='r')
imageCountryMap = imageCountryMap.resize((700, 525))
imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
countryMap_image.create_image(650, 350, image=imageCountryMap, anchor=CENTER)
countryMap_image.place(width=1280, height=720, relx=0.075, rely=-0.1)


# Function which loads the desired map
def click(number):
    '''
    A function that generates the emissions maps
    parameters
    ----------------------
    number: int
        An integer which selects the map to show: 1 is Canada, 2 is USA, 3 is North America
    '''
    global countryMap_path
    global imageCountryMap
    global countryMap_image
    global canada
    global usa
    global mexico
    if number == 1:
        # Generates map of Canada
        region_map(canada)
        countryMap_path = r"source\images\canada_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((700, 525))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(
            650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(width=1280, height=720, relx=0.075, rely=-0.1)
    elif number == 2:
        # Generates map of USA
        region_map(usa)
        countryMap_path = r"source\images\USA_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((700, 525))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(
            650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(width=1280, height=720, relx=0.075, rely=-0.1)
    elif number == 3:
        # Generates map of North America
        continent_map()
        countryMap_path = r"source\images\\continent_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((700, 525))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(
            650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(width=1280, height=720, relx=0.075, rely=-0.1)


# Buttons to select maps
Canada_path = "source\\images\\canada.png"
CanadaImage = Image.open(Canada_path, mode="r")
CanadaImage = CanadaImage.resize((int(width_px*0.25), 135))
CanadaImage = ImageTk.PhotoImage(CanadaImage, master=root)
USA_path = "source\\images\\USA.png"
USAImage = Image.open(USA_path, mode="r")
USAImage = USAImage.resize((250, 125))
USAImage = ImageTk.PhotoImage(USAImage, master=root)
NA_path = r"source\images\\NA.png"
NA_Image = Image.open(NA_path, mode="r")
NA_Image = NA_Image.resize((250, 125))
NA_Image = ImageTk.PhotoImage(NA_Image, master=root)

# Map page buttons
CanadaButton = Button(
    MapFrame,
    compound=TOP,
    width=100*(width_px/1536),
    height=100*(height_px/864),
    image=CanadaImage,
    command=lambda: click(1),
    relief=FLAT)
USAButton = Button(
    MapFrame,
    compound=TOP,
    width=100*(width_px/1536),
    height=100*(height_px/864),
    image=USAImage,
    command=lambda: click(2),
    relief=FLAT)
NA_Button = Button(
    MapFrame,
    compound=TOP,
    width=100*(width_px/1536),
    height=100*(height_px/864),
    image=NA_Image,
    command=lambda: click(3),
    relief=FLAT)

# Graph Page Initialization
create_pie_countries([canada, usa, mexico])
countryGraph_image = Canvas(GraphFrame)
countryGraph_path = "source\images/NA_pie.png"
imageCountryGraph = Image.open(countryGraph_path, mode='r')
imageCountryGraph = imageCountryGraph.resize((700, 525))
imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
countryGraph_image.create_image(650, 350, image=imageCountryGraph, anchor=CENTER)
countryGraph_image.place(width=1280, height=720, relx=-0.2, rely=0.1)


# Function which loads the desired graph
def clickGraph(number2):
    '''
    A function that generates the emissions Graphs, either as a Pie chart or a Bar chart
    parameters
    ----------------------
    number2: int
        An integer which selects the graph to show: 1 is Canada, 2 is USA, 3 is North America
    '''
    global countryGraph_path
    global imageCountryGraph
    global countryGraph_image
    global create_bar
    if number2 == 1:
        if create_bar:
            countryGraph_path = r"source\images\Canada_bar.png"
        else:
            countryGraph_path = r"source\images\Canada_pie.png"
        if not os.path.isfile(countryGraph_path) and create_bar:
            create_bar_regions(canada)
        if not os.path.isfile(countryGraph_path) and create_bar == False:
            create_pie_regions(canada)
        imageCountryGraph = Image.open(
            countryGraph_path, mode='r').resize(
            (700, 525))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(
            600, 350, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(width=1280, height=720, relx=0.119, rely=-0.1)
    elif number2 == 2:
        if create_bar:
            countryGraph_path = r"source\images\\USA_bar.png"
        else:
            countryGraph_path = r"source\images/USA_pie.png"
        if not os.path.isfile(countryGraph_path) and create_bar:
            create_bar_regions(usa)
        if not os.path.isfile(countryGraph_path) and create_bar == False:
            create_pie_regions(usa)
        imageCountryGraph = Image.open(
            countryGraph_path, mode='r').resize(
            (700, 525))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(
            600, 350, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(width=1280, height=720, relx=0.119, rely=-0.1)
    elif number2 == 3:
        countryGraph_path = r"source\images/NA_pie.png"
        if create_bar:
            countryGraph_path = "source\images/NA_bar.png"
        else:
            countryGraph_path = "source\images/NA_pie.png"
        if not os.path.isfile(countryGraph_path) and create_bar:
            create_bar_countries([canada, usa, mexico])
        if not os.path.isfile(countryGraph_path) and create_bar == False:
            create_pie_countries([canada, usa, mexico])
        imageCountryGraph = Image.open(countryGraph_path, mode='r').resize((700, 525))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(600, 350, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(width=1280, height=720, relx=0.119, rely=-0.1)


# Graph page buttons
CanadaButtonGraph = Button(
    GraphFrame,
    compound=TOP,
    width=100*(width_px/1536),
    height=100*(height_px/864),
    image=CanadaImage,
    command=lambda: clickGraph(1),
    relief=FLAT)
USAButtonGraph = Button(
    GraphFrame,
    compound=TOP,
    width=100*(width_px/1536),
    height=100*(height_px/864),
    image=USAImage,
    command=lambda: clickGraph(2),
    relief=FLAT)
NA_ButtonGraph = Button(
    GraphFrame,
    compound=TOP,
    width=100*(width_px/1536),
    height=100*(height_px/864),
    image=NA_Image,
    command=lambda: clickGraph(3),
    relief=FLAT)

# Switches between pie and bar graphs
toggle_image = "source\images/ToggleBar.png"


def graph_switch():
    '''
    A function that switches between the Pie and Bar graphs
    '''
    global create_bar
    global toggle_image
    global ToggleImage
    global GraphToggle
    global countryGraph_path
    create_bar = not create_bar
    country_list = ["Canada","USA","NA"]
    if not create_bar:
        toggle_image = "source\images/ToggleBar.png"
        ToggleImage = Image.open(toggle_image, mode="r")
        ToggleImage = ToggleImage.resize((100, 100))
        ToggleImage = ImageTk.PhotoImage(ToggleImage, master=root)
        GraphToggle = Button(
            GraphFrame,
            compound=TOP,
            width=100*(width_px/1536),
            height=100*(height_px/864),
            text="Switch Graph Types",
            command=lambda: graph_switch(),
            relief=FLAT,
            image=ToggleImage)
        GraphToggle.place(relx=0.055, rely=0.2, relwidth=0.1, relheight=0.15)
        for i in range(len(country_list)):
            if countryGraph_path.find(country_list[i]) != -1:
                clickGraph(i+1)
    else:
        toggle_image = "source\images/TogglePie.png"
        ToggleImage = Image.open(toggle_image, mode="r")
        ToggleImage = ToggleImage.resize((100, 100))
        ToggleImage = ImageTk.PhotoImage(ToggleImage, master=root)
        GraphToggle = Button(
            GraphFrame,
            compound=TOP,
            width=100*(width_px/1536),
            height=100*(height_px/864),
            text="Switch Graph Types",
            command=lambda: graph_switch(),
            relief=FLAT,
            image=ToggleImage)
        GraphToggle.place(relx=0.055, rely=0.2, relwidth=0.1, relheight=0.15)
        for i in range(len(country_list)):
            if countryGraph_path.find(country_list[i]) != -1:
                clickGraph(i+1)


graph_switch()

ToggleImage = Image.open(toggle_image, mode="r")
ToggleImage = ToggleImage.resize((100, 100))
ToggleImage = ImageTk.PhotoImage(ToggleImage, master=root)
GraphToggle = Button(
    GraphFrame,
    compound=TOP,
    width=100,
    height=100,
    text="Switch Graph Types",
    command=lambda: graph_switch(),
    relief=FLAT,
    image=ToggleImage)

# Places Menu buttons and Home page objects
GraphButton.place(
    anchor=NE,
    x=1,
    y=1,
    relx=1,
    relwidth=0.3333333333333333333333)
MapButton.place(relx=0.3333333333333333333333, x=1,
                y=1, relwidth=0.3333333333333333333333)
HomeButton.place(anchor=NW, x=1, y=1, relwidth=0.3333333333333333333333)
title_image.place(anchor=NW)
map_image.place(relx=0.4,rely=0.5)

# Places Map page buttons
NA_Button.place(relx=0.8, rely=0.7, relwidth=0.2, relheight=0.3)
CanadaButton.place(relx=0.055, rely=0.7, relwidth=0.2, relheight=0.3)
USAButton.place(relx=0.45, rely=0.7, relwidth=0.2, relheight=0.3)

# Graph Map page buttons
NA_ButtonGraph.place(relx=0.8, rely=0.7, relwidth=0.2, relheight=0.3)
CanadaButtonGraph.place(relx=0.055, rely=0.7, relwidth=0.2, relheight=0.3)
USAButtonGraph.place(relx=0.45, rely=0.7, relwidth=0.2, relheight=0.3)
GraphToggle.place(relx=0.055, rely=0.2, relwidth=0.1, relheight=0.15)

# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                   root.winfo_screenheight()))

# Exits application, deletes all maps/graphs
root.mainloop()
mapDelete('source/images/')
graphDelete('source/images/')

#if __name__ == '__main__':
