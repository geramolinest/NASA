import streamlit as st
import pandas as pd
import api
from PIL import Image

def Front():
    json_data = api.MarsWeather()
    dataframe = pd.json_normalize(json_data)

    st.set_page_config(page_title="NASA API REST",page_icon="C:/Users/estra/OneDrive/Escritorio/APINASA/Imagenes/nasa.jpg")
    st.title("Mars Weather")
    image = Image.open('C:/Users/estra/OneDrive/Escritorio/APINASA/Imagenes/nasa.jpg')
    st.image(image,width = 150)
    st.text("Fuente: " + str(api.getURL()))
    st.dataframe(dataframe)
    


if __name__=='__main__':
    Front()


    
    
    
