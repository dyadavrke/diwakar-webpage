import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title ="My Webpage", page_icon =":tada:", layout = 'wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/86481fe2-b1f5-4bd3-b90c-03d7b3b62cd3/eABcxDUigK.json")



#Header Section# 
with st.container():
    st.subheader("HI, I am Diwakar Yadav :wave:")
    st.title("A Data Scientist From India")
    st.write("I am passionate about uncovering insights from data to help grow business")
    st.write("[My Linkedin Profile >](https://www.linkedin.com/in/diwakar-yadav/)")


#

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write('##')
        st.write( 
            """
            I am currently working as Product Data scientist at Mastercard Data & Services within their Location Intelligence Product Suite. 
            I have done my Bachelor of engineering from IIT Bombay with major in Civil engineering where I developed a strong mathematical and engineering mindset.
            """
            
        )
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")


with st.container():
    st.write("---")
    st.header('Get in Touch with Me!')
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/diwakar.techfest@gmail.com" method="POST">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your email"  required>
     <textarea name = "message" placeholder = "Your Message here" required></textarea> 
     <button type="submit">Send</button>
</form> """

    left_column, right_column = st.columns(2) 
    with left_column: 
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column: 
        st.empty()

#using CSS 
def local_css(file_name):
    with open(file_name) as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")


