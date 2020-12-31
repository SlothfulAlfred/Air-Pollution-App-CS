import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.tools as tls
import numpy as np
import pandas as pd

scope= ['Canada']
dataFrame = pd.read_csv(r"C:\Users\johan\Downloads\Untitled spreadsheet - Sheet1.csv")
dataFrame_new = dataFrame[dataFrame['Province'].isin(scope)]

values = dataFrame_new['Pollution'].tolist()
colorscale = ["FF5733","FF5733","174AAF","17AF53",
              "17AF53","AF3217","FF5733","174AAF","AF3217","FF5733","174AAF","AF3217","17AF53",]
