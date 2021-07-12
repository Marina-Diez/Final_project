import streamlit as st
from PIL import Image
#import src.manage_data as dat
import plotly.express as px
import pandas as pd
import folium
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import numpy as np  
import codecs
import streamlit.components.v1 as components

# We write a tittle and add some photos

logo = Image.open("images/logo.jpg")

col1, col2, col3 = st.beta_columns([1,1,1])
col2.image(logo, use_column_width=True)

st.write("""
# Come visit Portugal 
""")

col1, col2 = st.beta_columns(2)

lisboa = Image.open("images/lisboa.jpg")
col1.header("Lisbon")
col1.image(lisboa, use_column_width=True)

algarve = Image.open("images/algarve.jpg")
col2.header("Algarve")
col2.image(algarve, use_column_width=True)

st.title('Select you perfect option')

# We make all selection parametres

destinations_names = ["Lisbon","Algarve"]
destination = st.radio("Where do you prefer to go?", destinations_names)
days_left = st.number_input("In how many days would you arrive?", format="%.0f")
year = st.number_input("Year:",format="%.0f")
month = st.number_input("Month:", format="%.0f")
day = st.number_input("Day of the month:", format="%.0f")
weekend = st.number_input("Nº of weekend days:", format="%.0f")
week = st.number_input("Nº of non weekend days:", format="%.0f")
adult = st.number_input("Nº of adults:", format="%.0f")
children = st.number_input("Nº of children:", format="%.0f")
babies = st.number_input("Nº of babies:", format="%.0f")
meals_names = ["No meal package","Bed & Breakfast", "Half board", "Full board"]
meals = st.radio("Which meal option do you prefer?", meals_names)
room_names = ["Standard Individual","Standard Double", "Premium", "Suite", "Suite extra"]
room = st.radio("Which type of room do you prefer?", room_names)
requests = st.number_input("Special requests: how many of the following request would you like? twin bed,Separate beds, Baby crib, Temporary bed, Room breakfast service or/and Extra pillow", format="%.0f")

# We put all parametres on a data frame
data = {"hotel":destination,
                "lead_time":days_left,
                "arrival_date_year":year,
                "arrival_date_month":month,
                "arrival_date_day_of_month":day,
                "stays_in_weekend_nights": weekend,
                "stays_in_week_nights": week,
                "adults": adult,
                "children": children,
                "babies": babies,
                "meal": meals,
                "reserved_room_type": room,        
                "total_of_special_requests": requests
                }
                
df = pd.DataFrame(data, index=[0])
# We repeat all changes we have done to our dataset to optimize our values and do not have categorical ones.
le = preprocessing.LabelEncoder()
df["hotel"] = le.fit_transform(df["hotel"])


dic_meal = {"No meal package": 1,
            "Bed & Breakfast": 2,
            "Half board":3,
            "Full board":5
               }
df["meal"] = df["meal"].map(dic_meal)

dic_room = {"Standard Individual": 2,
            "Standard Double":3,
            "Premium": 6,
            "Suite":8,
             "Suite extra":9
               }
df["reserved_room_type"] = df["reserved_room_type"].map(dic_room)

# We decide to select the model that do not use normalization

load = pickle.load(open("./model/modelo3.pkl", "rb"))

if st.button('Get price'): #making and printing our prediction
    result = load.predict(df)
    result = np.round(result, 2).astype(float)
    st.write(f' {result} € / per nigth')  






