import streamlit as st
import pandas as pd
from PIL import Image
with st.container():
    st.write("---")

    st.title("Contact:")
    st.write("##")
image =Image.open('dp.png')
st.image(image, width=600)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
 
  
txt2('LinkedIn', 'https://www.linkedin.com/in/manas-kumar-giri-377756251/')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/MANAS8991/apuu')
txt2('Facebook', 'https://www.facebook.com/profile.php?id=100009202998579')
txt2('Instagram', 'https://www.instagram.com/manaskumar_111/')
txt2('Whats app', '9178572597 // 6370830639 // 7077853598 // 90901550750')

def main():
    st.title("Location")


    data = {
        'latitude': [21.929966049982852],
        'longitude': [86.76586103524697]
    }
    df = pd.DataFrame(data)
    
    # Display the map with your location
    st.map(df, zoom=10)
    
    # Generate the URL link to your location
    latitude = df['latitude'].values[0]
    longitude = df['longitude'].values[0]
    location_url = f"https://maps.google.com/?q={latitude},{longitude}"
    
    # Display the URL link
    st.header("Click To Get Location")
    st.markdown(f"[Click here to view location]({location_url})")
    
    
    
    
if __name__ == "__main__":
    main()