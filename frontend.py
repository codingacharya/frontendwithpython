import streamlit as st
import os

# Page configuration
st.set_page_config(page_title='My Streamlit Website', layout='wide')

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])

# Carousel using Streamlit
image_folder = "images"  # Change this to your local image folder path
image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(("png", "jpg", "jpeg"))]

# Display images as a slideshow
if image_files:
    img_index = st.session_state.get("img_index", 0)
    st.image(image_files[img_index], use_column_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous"):
            st.session_state.img_index = (img_index - 1) % len(image_files)
    with col2:
        if st.button("Next"):
            st.session_state.img_index = (img_index + 1) % len(image_files)
else:
    st.warning("No images found in the 'images' folder!")

# Main Content
if menu == "Home":
    st.header("Welcome to My Website")
    st.write("This is a simple Streamlit website with a menu, footer, and image slideshow.")
elif menu == "About":
    st.header("About Us")
    st.write("We are building amazing projects with Streamlit!")
elif menu == "Contact":
    st.header("Contact Us")
    st.write("Email: contact@mywebsite.com")

# Footer
footer = """
    <style>
        .footer {position: fixed; bottom: 0; width: 100%; background: lightgray; text-align: center; padding: 10px;}
    </style>
    <div class="footer">© 2025 My Streamlit Website. All Rights Reserved.</div>
    """
st.markdown(footer, unsafe_allow_html=True)
