import streamlit as st
from main import main
from eda import eda
import urllib.request
from PIL import Image
def main_page():
    menu = ["Home", "Prediction Section", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":

        st.write("## Bike rental Demand Prediction")

        urllib.request.urlretrieve(
            'http://betterbikeshare.org/wp-content/uploads/2015/06/BikeShareLaunch.227.jpg',
            "gfg.png")

        img = Image.open("gfg.png")
        st.image(img)

        st.write(
            """

### - App Content
 - This app has 3 sections

 1) Home Page - The page you are currently in

 


 2) Prediction- The page in which you will be asked to give the information on all the required aspects
   and we will predict the desired the output
   
 3) About - This Page is about me
       """)

    elif choice == "Data Analysis Section":
        eda()
    elif choice == "Prediction Section":
        main()
    else:
        st.subheader("About")
        st.write("""
          #### Name :- punith
          #### Email:-puniuday493@gmail.com
          #### Github link- https://github.com/puniuday""")



main_page()