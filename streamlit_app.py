import streamlit as st
from PIL import Image

st.set_page_config(
page_title="Klasifikasi Apel",
page_icon="🍎"
)

st.title("🍎 Klasifikasi Apel")

uploaded_file = st.file_uploader(
"Upload gambar apel",
type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
image = Image.open(uploaded_file)

```
st.image(
    image,
    caption="Gambar yang diupload",
    use_container_width=True
)

st.success("File berhasil diupload")

st.write("Prediksi sederhana:")

image_rgb = image.convert("RGB")

pixels = list(image_rgb.getdata())

total_r = 0
total_g = 0

for r, g, b in pixels:
    total_r += r
    total_g += g

avg_r = total_r / len(pixels)
avg_g = total_g / len(pixels)

if avg_g > avg_r:
    st.success("🍏 Apel Hijau")
else:
    st.success("🍎 Apel Merah")
