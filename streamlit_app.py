import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Klasifikasi Gambar Apel",
    page_icon="🍏",
    layout="centered"
)

st.title("🍏 Klasifikasi Gambar Apel")

uploaded_file = st.file_uploader(
    "Pilih gambar",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Gambar yang diupload",
        use_container_width=True
    )

    img = image.resize((128, 128))
    img = np.array(img, dtype=np.float32) / 255.0

    st.subheader("Informasi Gambar")

    st.write(f"Shape gambar: {img.shape}")
    st.write(f"Nilai minimum: {img.min():.4f}")
    st.write(f"Nilai maksimum: {img.max():.4f}")

    st.success("Gambar berhasil diproses")
