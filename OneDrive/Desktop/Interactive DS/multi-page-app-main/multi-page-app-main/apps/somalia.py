import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    @st.cache
    def load(url):
        return pd.read_json(url)

    path = "C:/Users/hamsi/OneDrive/Desktop/Interactive DS/multi-page-app-main/multi-page-app-main/Datasets1/natural-disasters.csv"
    water= "C:/Users/hamsi/OneDrive/Desktop/Interactive DS/Datasets1/water-somalia.csv"
    disaster= "C:/Users/hamsi/OneDrive/Desktop/Interactive DS/Datasets1/disasters-somalia.csv"
     

   
    df = pd.read_csv(water)
    df2 = pd.read_csv(disaster)
    st.title('The Country with the highest drought risk index in the world') #look at book and make this better
    #put somlia map
    from PIL import Image
    image = Image.open("C:/Users/hamsi/OneDrive/Desktop/Interactive DS/Datasets1/country-somalia.png")

    st.image(image, caption='Somalia Map')
    #water levels
    import altair as alt
    
    st.header('Water')
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['Year'], empty='none')

    # The basic line
    line = alt.Chart(df).mark_line(interpolate='basis').encode(
        x='Year:Q',
        y='Water',
        color='Category:N'
    )
    

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(df).mark_point().encode(
        x='Year:Q',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'Water:Q', alt.value(' '))
    )
    # Draw a rule at the location of the selection
    rules = alt.Chart(df).mark_rule(color='gray').encode(
        x='x:Q',
    ).transform_filter(
        nearest
    )

    # Put the five layers into a chart and bind the data
    chart = alt.layer(
        line, selectors, points, rules, text
    ).properties(
        width=600, height=300
    )
    st.write(chart)
  
    st.header('Natural disasters')
    #natural disasters - drought
    
    chart2 = alt.Chart(df2).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1
    ).encode(
        alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
        alt.Y('Number of total people affected by drought:Q'),
        alt.Size('Number of deaths from disasters:Q',
            scale=alt.Scale(range=[0, 4000]),
            legend=alt.Legend(title='Annual Deaths from drought')
            
        ),
        alt.Color('Entity:N', legend=None)
         
    ).properties(
        width=450,
        height=320
    ).transform_filter(
        alt.datum.Entity != 'All natural disasters'
    
    )

    st.write(chart2)
   
    