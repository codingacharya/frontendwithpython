import streamlit as st
import time

# Page configuration
st.set_page_config(page_title='My Streamlit Website', layout='wide')

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])

# Carousel (Image Slideshow using HTML & JS)
carousel_html = '''
<div class="slideshow-container">
  <div class="mySlides fade">
    <img src="in1.jpeg" style="width:100%">
  </div>
  <div class="mySlides fade">
    <img src="in2.jpeg" style="width:100%">
  </div>
  <div class="mySlides fade">
    <img src="in3.jpeg" style="width:100%">
  </div>
</div>
<script>
let slideIndex = 0;
showSlides();
function showSlides() {
  let slides = document.getElementsByClassName("mySlides");
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1;}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 3000);
}
</script>
'''
st.components.v1.html(carousel_html, height=450)

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
st.components.v1.html(footer)
