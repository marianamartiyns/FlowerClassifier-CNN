import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

st.header('Modelo CNN de classificação de flores')
flower_names = ['Dente de Leao','Girassois', 'Margaridas', 'Rosas','Tulipas']

# Carregar o modelo completo
try:
    model = load_model('Flower_Recog_Model.keras')
    st.write("Modelo carregado com sucesso!")
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

def classify_images(image_path):
    try:
        input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
        input_image_array = tf.keras.utils.img_to_array(input_image)
        input_image_exp_dim = tf.expand_dims(input_image_array,0)

        predictions = model.predict(input_image_exp_dim)
        result = tf.nn.softmax(predictions[0])
        outcome = 'Essa imagem pertence ao grupo de ' + flower_names[np.argmax(result)] + ' com uma precisão de '+ str(np.max(result)*100)
        return outcome
    except Exception as e:
        return f"Erro ao classificar a imagem: {e}"

uploaded_file = st.file_uploader('Upload an Image')
if uploaded_file is not None:
    # Salvar o arquivo enviado pelo usuário temporariamente
    try:
        upload_dir = 'upload'
        os.makedirs(upload_dir, exist_ok=True)  # Certificar-se de que o diretório existe
        with open(os.path.join(upload_dir, uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        st.image(uploaded_file, width=200)

        st.write("Classificação da Imagem:")
        image_path = os.path.join(upload_dir, uploaded_file.name)
        st.markdown(classify_images(image_path))
    except Exception as e:
        st.error(f"Erro ao processar a imagem: {e}")

