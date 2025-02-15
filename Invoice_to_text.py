# you will need to input your api key


from dotenv import load_dotenv
import streamlit as st  
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()   

genai.configure(api_key="")

## function to load gemini pro vision

model= genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
  
    
    if uploaded_file is not None:
        try:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()
            return bytes_data
        except Exception as e:
            print(f"Error converting image to bytes: {str(e)}")
            return None
    return None


st.set_page_config(page_title="Gemini Image Demo", page_icon="🔮", layout="wide")

st.header("Multi Language Invoice Extractor")
input= st.text_input("Input prompt : ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """You are an expert in understanding invoices.
                We will upload an image as invoice and you will have to asnwer any questions based on
                 the uploaded invoice. """


# if submit is clicked

if submit:
    image_data= input_image_details(uploaded_file)
    response= get_gemini_response(input, image_data, input_prompt)
    st.subheader("Response is ")
    st.write(response)
      

