import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
page_title="Klasifikasi Apel",
page_icon="🍎",
layout="centered"
)

st.title("🍎🍏 Klasifikasi Apel Merah dan Hijau")

uploaded_file = st.file_uploader(
"Upload gambar apel",
type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

```
image = Image.open(uploaded_file).convert("RGB")

st.image(
    image,
    caption="Gambar yang diupload",
    use_container_width=True
)

img = image.resize((128, 128))
img = np.array(img)

red_mean = np.mean(img[:, :, 0])
green_mean = np.mean(img[:, :, 1])
blue_mean = np.mean(img[:, :, 2])

st.subheader("Analisis Warna")

st.write(f"Merah (R): {red_mean:.2f}")
st.write(f"Hijau (G): {green_mean:.2f}")
st.write(f"Biru (B): {blue_mean:.2f}")

if green_mean > red_mean:
    st.success("🍏 Prediksi: Apel Hijau")
else:
    st.success("🍎 Prediksi: Apel Merah")
