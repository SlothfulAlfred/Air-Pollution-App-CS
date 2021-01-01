import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
df = pd.read_csv(r"C:\Users\johan\Downloads\data.csv") #Change the file path to work on your device
geojson = json.load(open("C:\Users\johan\Downloads\canada_provinces.geojson", "r")) #Change the file path to work on your device

prov_id_map = {}
for feature in geojson["features"]:
    feature["id"] = feature["properties"]["cartodb_id"]
    prov_id_map[feature["properties"]["name"]] = feature["id"]

df = pd.read_csv("C:\Users\johan\Downloads\data.csv")
df["Density"] = df["Pollution"].apply(lambda x: int(x))
df["id"] = df["Province"].apply(lambda x: prov_id_map[x])
df.head()

df["DensityScale"] = np.log10(df["Density"])
fig = px.choropleth(
    df,
    locations="id",
    geojson=geojson,
    color="DensityScale",
    hover_name="Province",
    hover_data=["Density"],
    title="India Population Density",
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
fig.write_image('C:/Users/johan/Desktop/fig1.png') #Change the file path to work on your device
fig.to_image(format="png", engine="kaleido")
#If this works correctly, the program will open a tab (I'm not sure if the tab has the graph) and generate a png file of the graph at the specified location
