import streamlit as st

st.title("🎈 Aplikasi Rachma")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
action = st.menu_button("Export", options=["nama", "asal", "umur"])
if action == "nama":
    st.write("Kiki")
elif action == "asal":
    st.write("Bogor")
elif action == "umur":
    st.write("20 tahun")
