#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:21:44 2020

@author: awinecoff
"""

import os
import database_conn
import pandas as pd
import vertica_python
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hexfg
from matplotlib.patches import Polygon
import numpy as np


import plotly as py
import plotly.graph_objs as go

#Load the data
import petprofile_data_extraction

med_cond_sum = med_condition_df[['pet_med_condition_nm', 'med_condition']].groupby(['pet_med_condition_nm']).sum().reset_index()


state_sum = pet_customer_df[['us_state', 'pet_id']].groupby(['us_state']).count().reset_index()


data = dict (
    type = 'choropleth',
    locations = state_sum['us_state'],
    locationmode='USA-states',
    colorscale = 'viridis',
    z=state_sum['pet_id'])

lyt = dict(geo=dict(scope='usa'))
us_map = go.Figure(data=[data], layout = lyt)
py.offline.plot(us_map)