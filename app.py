import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title(" Image to Text App ")

st.markdown("")

image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("Image converting"):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] 


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

