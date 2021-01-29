# -----------------------------------------------------
# Name:             NA CO2 Tracker (main.py)
# Purpose:          To create an app to raise awareness about climate change and air pollution in North America
#
#
#
# Author:           Alfred Mikhael, 627582: Rishabh Tamhane, 813403: Johann Zhao, 620988
# Created:          27-Sep-2020
# Updated:          29-Jan-2021
# References:       All coordinate data is taken from https://www.latlong.net/category/states-236-14.html.
#                   Greenhouse gas statistics are taken from Stats Canada or US Energy Information Administration
#                   for Canadian and American values respectively.
# ----------------------------------------------------
import os

from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
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

# Initialize Country objects used for maps and graphs
canada = Country("docs/canada.txt")
usa = Country("docs/usa.txt")
mexico = Country("docs/mexico.txt")

# Clears any pre-generated maps
mapDelete('source/images/')
graphDelete('source/images/')
create_bar = True

# Initializing of title and icon image
root.title('NA CO2 Tracker')
Icon_path = r"source\images\\icon.png"
Icon = Image.open(Icon_path, mode="r")
Icon = ImageTk.PhotoImage(file=Icon_path, master=root)
root.iconphoto(False, Icon)

# Footer which links to Source Code
Footer_path = r"source\images\\footer.png"
Footer = Image.open(Footer_path, mode="r")
Footer = Footer.resize((19, 19))
Footer = ImageTk.PhotoImage(Footer)

helv24 = tkFont.Font(family='Helvetica',
        size=24)

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

tips = Button(
    text="What Can I Do?",
    compound=LEFT,
    command=lambda: webbrowser.open("Actions.txt"),
    relief=FLAT)
tips.place(relwidth=0.08, relheight=0.0277777777777778, rely=0.9525, relx=0.01)

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

title = Canvas(HomeFrame, height=300*(height_px/864), width=width_px)
title.create_text(795*(width_px/1536), 150*(height_px/864), text="NA CO2 Tracker"
                        ,font=("Helvetica",35))

credit = Canvas(height=50*(height_px/864), width=400*(width_px/1536))
credit.create_text(200*(width_px/1536), 15*(height_px/864), text="Made by: Alfred Mikhael, Rishabh Tamhane, Johann Zhao")
credit.place(anchor=S, relx=0.48, rely=1.02)

title_image = Canvas(HomeFrame, height=300*(height_px/864), width=width_px)
titleimage_path = r"source\images\\titleimage.png"
image = Image.open(titleimage_path, mode="r")
image = image.resize((int(width_px*1.25),int(300*(height_px/864))))
image = ImageTk.PhotoImage(image, master=root)
title_image.create_image(600*(width_px/1536),150*(height_px/864), image=image)
title_image.create_rectangle(0, 0, width_px, int(300*(height_px/864)), fill='grey', stipple='gray75')
title_image.create_text(750*(width_px/1536), 100*(height_px/864), width=width_px-50, text="An application that graphically and geographically displays CO2 emissions of Canada and the USA. With the aim of reducing the effects of climate change, " \
"our application will provide statistical and visual methods of understanding the impact of some of the world's largest CO2 emitting countries on the Earth's climate, based on data from reputable sources. \n Started: Nov 30, 2020."
                        , font=("Helvetica",14))

intro = Canvas(HomeFrame, height=300*(height_px/864), width=550*(width_px/1536))
intro.create_text( 250,150,width=450,
text = "In the modern day, keeping countries accountable for the CO2 emissions is becoming increasingly difficult. CO2 levels are currently significantly higher than at any point in the past 800,000 years and since 1980, they have increased 22% at a consistent rate. In North America, Canada and the US are huge contributors to this global issue, as their CO2 emissions per capita are significantly higher than other coutnries. Despite being only the 3rd and 39th most populous country in the world, they produce the 2nd and 11th most CO2 emissions. Overall, the main reason for this is that there are very few ways for the general public to understand the scope of their emissions. We aim to change that.")

map_image = Canvas(HomeFrame, height=300, width=300)
mapimage_path = r'source\images\mapimage.jpg'
image2 = Image.open(mapimage_path, mode="r")
image2 = image2.resize((300, 300))
image2 = ImageTk.PhotoImage(image2, master=root)
map_image.create_image(150, 150, image=image2, anchor=CENTER)
map_image.create_rectangle(0, 0, 300, 300, fill='grey', stipple='gray75')
map_image.create_text(
    150,
    150,
    width=300,
    text="See what regions in North America have the greatest levels of pollution.")

stat = Canvas(HomeFrame, height=100, width=600)
stat.create_text(325,70,
    text="Statistics for over 60 states,\n provinces and territories",font=helv24)
stat.create_text(1000,70,
    text="Open Source with \n long-term support plans",font=helv24)

graph_image = Canvas(HomeFrame, height=300, width=300)
graphimage_path = r'source\images\graphimage.png'
image3 = Image.open(graphimage_path, mode="r")
image3 = image3.resize((300, 300))
image3 = ImageTk.PhotoImage(image3, master=root)
graph_image.create_image(150, 150, image=image3, anchor=CENTER)
graph_image.create_rectangle(0, 0, 300, 300, fill='grey', stipple='gray75')
graph_image.create_text(
    150,
    150,
    width=300,
    text="View the carbon emissions of North America and it's consituent countries as graphs: pie or bar charts are currently available.")


# Map Page Initialization
continent_map()
countryMap_image = Canvas(MapFrame)
countryMap_path = r"source\images\\continent_map.png"
imageCountryMap = Image.open(countryMap_path, mode='r')
imageCountryMap = imageCountryMap.resize((700, 525))
imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
countryMap_image.create_image(650, 350, image=imageCountryMap, anchor=CENTER)
countryMap_image.place(relwidth=1280/1536, relheight=720/864, relx=0.07, rely=-0.1)


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
        countryMap_image.place(relwidth=1280/1536, relheight=720/864, relx=0.07, rely=-0.1)
    elif number == 2:
        # Generates map of USA
        region_map(usa)
        countryMap_path = r"source\images\USA_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((700, 525))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(
            650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(relwidth=1280/1536, relheight=720/864, relx=0.07, rely=-0.1)
    elif number == 3:
        # Generates map of North America
        continent_map()
        countryMap_path = r"source\images\\continent_map.png"
        imageCountryMap = Image.open(countryMap_path, mode='r')
        imageCountryMap = imageCountryMap.resize((700, 525))
        imageCountryMap = ImageTk.PhotoImage(imageCountryMap, master=root)
        countryMap_image.create_image(
            650, 350, image=imageCountryMap, anchor=CENTER)
        countryMap_image.place(relwidth=1280/1536, relheight=720/864, relx=0.07, rely=-0.1)


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
countryGraph_image.place(relwidth=1280/1536, height=720/864, relx=0.2, rely=-0.1)


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
        if not os.path.isfile(countryGraph_path) and not create_bar:
            create_pie_regions(canada)
        imageCountryGraph = Image.open(
            countryGraph_path, mode='r').resize(
            (665, int(498*(height_px/864))))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(
            600, 350, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(relwidth=1280/1536, relheight=720/864, relx=0.1, rely=-0.1)
    elif number2 == 2:
        if create_bar:
            countryGraph_path = r"source\images\\USA_bar.png"
        else:
            countryGraph_path = r"source\images/USA_pie.png"
        if not os.path.isfile(countryGraph_path) and create_bar:
            create_bar_regions(usa)
        if not os.path.isfile(countryGraph_path) and not create_bar:
            create_pie_regions(usa)
        imageCountryGraph = Image.open(
            countryGraph_path, mode='r').resize(
            (665, int(498*(height_px/864))))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(
            600, 350, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(relwidth=1280/1536, relheight=720/864, relx=0.1, rely=-0.1)
    elif number2 == 3:
        countryGraph_path = r"source\images/NA_pie.png"
        if create_bar:
            countryGraph_path = "source\images/NA_bar.png"
        else:
            countryGraph_path = "source\images/NA_pie.png"
        if not os.path.isfile(countryGraph_path) and create_bar:
            create_bar_countries([canada, usa, mexico])
        if not os.path.isfile(countryGraph_path) and not create_bar:
            create_pie_countries([canada, usa, mexico])
        imageCountryGraph = Image.open(countryGraph_path, mode='r').resize((700, 525))
        imageCountryGraph = ImageTk.PhotoImage(imageCountryGraph, master=root)
        countryGraph_image.create_image(600, 350, image=imageCountryGraph, anchor=CENTER)
        countryGraph_image.place(relwidth=1280/1536, relheight=720/864, relx=0.1, rely=-0.1)


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
        GraphToggle.place(relx=0.055, rely=0.2, relwidth=0.1, relheight=0.2)
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
        GraphToggle.place(relx=0.055, rely=0.2, relwidth=0.1, relheight=0.2)
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
title.place(anchor = N,relx=0.495,rely=-0.1)
title_image.place(anchor=NW,rely = 0.15)
stat.place(rely=0.4,relwidth=1,relx =0,relheight=0.2)
intro.place(relx=0.0,rely=0.5)
map_image.place(relx=0.4,rely=0.6)
graph_image.place(relx=0.7,rely=0.6)

# Places Map page buttons
NA_Button.place(relx=0.77, rely=0.75, relwidth=0.18, relheight=0.27)
CanadaButton.place(relx=0.05, rely=0.75, relwidth=0.18, relheight=0.27)
USAButton.place(relx=0.40, rely=0.75, relwidth=0.18, relheight=0.27)

# Graph Map page buttons
NA_ButtonGraph.place(relx=0.77, rely=0.75, relwidth=0.18, relheight=0.27)
CanadaButtonGraph.place(relx=0.05, rely=0.75, relwidth=0.18, relheight=0.27)
USAButtonGraph.place(relx=0.40, rely=0.75, relwidth=0.18, relheight=0.27)
GraphToggle.place(relx=0.055, rely=0.2, relwidth=0.1, relheight=0.2)

# Set size of window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                   root.winfo_screenheight()))

# Exits application, deletes all maps/graphs
root.mainloop()
mapDelete('source/images/')
graphDelete('source/images/')

#if __name__ == '__main__':
