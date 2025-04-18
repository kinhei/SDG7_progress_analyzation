import os
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import numpy as np

import pandas as pd 
import seaborn as sns
import colorcet as cc
import cmasher as cmr

import plotly.graph_objects as go
import plotly.io as pio

import networkx as nx

from utils import set_rcParams

os.makedirs("../figures", exist_ok=True)

fontsize = 20
rcParams = {'figure.labelsize':fontsize, 'axes.labelsize':fontsize, 'xtick.labelsize':fontsize, 
            'ytick.labelsize':fontsize, 'legend.fontsize':fontsize, 'figure.titlesize':fontsize, 
            'legend.title_fontsize':fontsize, 
            'axes.titlesize':fontsize, 'legend.frameon':False}
set_rcParams(**rcParams)