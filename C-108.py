import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly

df = pd.read_csv("D:\code\python\dataC-108.csv")

#fig = ff.create_distplot([df["Height"].tolist()],["Height"], show_hist = False)
fig = ff.create_distplot([df["Weight"].tolist()],["Weight"])
plotly.offline.plot(fig)