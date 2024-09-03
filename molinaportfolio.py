import streamlit as st
from PIL import Image

# Function to crop the image to a 16:9 aspect ratio
def crop_to_aspect(image, aspect_ratio=(16, 9)):
    img_width, img_height = image.size
    target_width = img_width
    target_height = int(target_width / aspect_ratio[0] * aspect_ratio[1])

    if target_height > img_height:
        target_height = img_height
        target_width = int(target_height * aspect_ratio[0] / aspect_ratio[1])

    left = (img_width - target_width) / 2
    top = (img_height - target_height) / 2
    right = (img_width + target_width) / 2
    bottom = (img_height + target_height) / 2

    return image.crop((left, top, right, bottom))

# Set the title of the app
st.title("Richard Roda Molina - This is my MOVING FORWARD story")

# Introduction with Picture
st.header("Autobiography")

# Create two columns
col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    Hello! I'm Richard Roda Molina, the 40th President of the Supreme Student Government, and the developer of the flagship program Project Forward. 
    I am passionate about leadership, innovation, and making a positive impact in my community. Below, you can explore some of my key achievements and projects.
    """)

with col2:
    # Display an introductory picture
    image = Image.open("intro_picture.jpg")  # Replace with your image path
    cropped_image = crop_to_aspect(image)
    st.image(cropped_image, use_column_width=True)

# Portfolio Section
st.header("Portfolio")

# Project Descriptions
st.subheader("1. Project Forward")
st.write("""
As the President of the Supreme Student Government, I developed Project Forward, a program aimed at enhancing student engagement and providing support to students in various aspects of their academic life. 
The program includes initiatives such as the SSG Scholarship Program and the Blue Ribbon Committee.
""")

st.subheader("2. Angkas Diaries")
st.write("""
I am also an Angkas Student Ambassador and have created content for Angkas Diaries, sharing my experiences and insights to promote road safety and responsible riding among students.
""")

st.subheader("3. CSS Extension Program")
st.write("""
During my time as the President of the CIT-U Computer Students’ Society, I led the CSS Extension Program, which included the CSS Tutorials and partnered with Cebu City National High School for the Clean Up Drive.
""")

# Gallery Slideshow with Navigation Buttons
st.subheader("Gallery Slideshow")

# List of images and captions
images = [
    {"image": "project_forward.jpg", "caption": "Project Forward"},
    {"image": "angkas_diaries.jpg", "caption": "Angkas Diaries"},
    {"image": "css_extension.jpg", "caption": "CSS Extension Program"}
]

# Initialize or retrieve current index from session state
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Display the current image
image = Image.open(images[st.session_state.current_index]['image'])
cropped_image = crop_to_aspect(image)
st.image(cropped_image, caption=images[st.session_state.current_index]['caption'], use_column_width=True)

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button('Previous'):
        st.session_state.current_index -= 1
        if st.session_state.current_index < 0:
            st.session_state.current_index = len(images) - 1

with col3:
    if st.button('Next'):
        st.session_state.current_index += 1
        if st.session_state.current_index >= len(images):
            st.session_state.current_index = 0

# Contact Information
st.header("Contact Information")
st.write("""
- **Email:** richard.molina@cit.edu / ssg@cit.edu
- **LinkedIn:** [Richard Roda Molina](https://www.linkedin.com/in/richardmolina1047/)
""")

# Footer
st.write("Thank you for visiting my portfolio! Feel free to reach out if you have any questions or opportunities for collaboration.")
