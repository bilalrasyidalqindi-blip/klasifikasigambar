import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "model_apel_cnn.h5",
        compile=False
    )

model = load_model()

st.set_page_config(
    page_title="Klasifikasi Gambar",
    page_icon="🖼️",
    layout="centered"
)

@st.cache_resource
def load_cnn_model():
    return 

try:
    model = load_cnn_model()
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

st.title("🖼️ Klasifikasi Gambar CNN")

uploaded_file = st.file_uploader(
    "Upload gambar",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Gambar Input",
        use_container_width=True
    )

    img = image.resize((128, 128))
    img = np.array(img, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    try:
        prediction = model.predict(
            img,
            verbose=0
        )

        st.subheader("Hasil Prediksi")

        if prediction.shape[-1] == 1:

            score = float(prediction[0][0])

            st.write(
                f"Probabilitas: {score:.4f}"
            )

            if score >= 0.5:
                st.success("Kelas 1")
            else:
                st.warning("Kelas 0")

        else:

            kelas = int(np.argmax(prediction))

            st.success(
                f"Kelas Prediksi: {kelas}"
            )

            st.write(prediction)

    except Exception as e:
        st.error(
            f"Terjadi kesalahan saat prediksi: {e}"
        )
