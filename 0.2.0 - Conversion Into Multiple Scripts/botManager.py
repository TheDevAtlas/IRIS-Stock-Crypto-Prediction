# Jacob McGowan 2021 #
# Create Or Load Bot For Use #

# Imports For Data Display And Manipulation
import datetime as dt # The Date And Time
import numpy as np # Basic Functions
import pandas as pd # Data Manipulation And Translations
import matplotlib.pyplot as plt # Visualization

# Imports From The Web
import pandas_datareader as web # Yahoo Finance, World Bank, Ect

# Imports For Machine Learning
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

def createNewBot():
    print("New Bot")
    # Create Bot From Atrabutes Given From botMain
    # Save The Bot With A New Name To A File

def trainBot():
    print("Train Bot")
    # Load Bot Name Given From botMain
    # Setup The Training Numbers Given From botMain
    # Run The Training
    # Save The Bot

def runBot():
    print("Run Bot")
    # Load Bot Name Given From botMain
    # Setup The Training Numbers Given From botMain
    # Run The Prediction
    # Output Data To Text File
    # Output Data To A Graph
