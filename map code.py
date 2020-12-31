import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.tools as tls
import numpy as np
import pandas as pd
# Also can you put a link to the documentation that you're using so that I know
# what params you need and what type of map you are making. I went to the plotly website
# and there are more than 10 different types of maps and I have no idea which you plan
# to use. 

scope= ['Canada']
# Why are you reading from a spreadsheet? The data is already on a file named "data.txt"
# and it will be initialized to objects later; it never passes through a spreadsheet phase. 
# Also, why is the filepath still not relative? 
dataFrame = pd.read_csv(r"C:\Users\johan\Downloads\Untitled spreadsheet - Sheet1.csv")

# Did you put an unnecessary layer of nesting here? why dataFrame[dataFrame[..]..] instead of just 
# [dataFrame[province] for province in scope] or [dataFrame[province] if dataFrame[province].isin(scope)]
# What I mean is that using list comprehension would be a better way to do this

dataFrame_new = dataFrame[dataFrame['Province'].isin(scope)]

values = dataFrame_new['Pollution'].tolist()
colorscale = ["FF5733","FF5733","174AAF","17AF53",
              "17AF53","AF3217","FF5733","174AAF","AF3217","FF5733","174AAF","AF3217","17AF53",]
