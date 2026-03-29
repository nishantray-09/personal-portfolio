import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Nishant Ray | Product Leader", page_icon="💼", layout="wide")

# 2. Advanced Styling (UPDATED TO DARK BLUE THEME)
st.markdown("""
    <style>
    /* Main Background: Dark Blue */
    .stApp { 
        background-color: #0a192f; 
    }
    
    /* Profile Photo Frame */
    [data-testid="stImage"] {
        border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); 
        max-width: 280px; 
        margin: auto;
        border: 2px solid #172a45;
    }
    
    /* Text Colors & Sizes */
    .main-text { font-size: 1.15rem; line-height: 1.8; color: #8892b0; }
    h1, h2, h3 { color: #ccd6f6 !important; font-weight: 700; }
    
    /* Contact Form Styling */
    input, textarea {
        background-color: #172a45 !important;
        color: #ccd6f6 !important;
        border: 1px solid #233554 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        width: 100% !important;
        margin-bottom: 12px !important;
    }
    
    /* Button Styling */
    .submit-btn {
        background-color: #64ffda;
        color: #0a192f;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
        font-weight: bold;
    }

    /* Section Dividers */
    hr { border: 0; height: 1px; background: #233554; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="large")
with col1:
    try:
        st.image("profile_pic.png")
    except:
        st.image("https://via.placeholder.com/280x350")

with col2:
    st.title("Nishant Ray")
    st.subheader("Product Lead | Automation Architect | Strategy & Execution")
    st.write("📍 Gurugram, India")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nishant-ray-08222810a/)")

# --- EXECUTIVE SUMMARY ---
st.write("---")
st.header("📌 Executive Summary")
st.write(f"""
<div class="main-text">
As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over six years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions—empowering teams to automate processes, optimize workflows, and deliver impactful results.<br><br>
My expertise spans team management, capacity planning, and forecasting, complemented by a strong foundation in competitive intelligence, product management, data analytics, and data visualization.<br><br>
I am passionate about transforming complex challenges into clean, efficient code, enabling businesses to scale seamlessly and automate repetitive tasks. Driven by strategic thinking and a collaborative leadership style, I excel at aligning cross-functional teams with business objectives, ensuring projects are delivered on time and exceed expectations. Whether guiding product vision or architecting automation solutions, I am dedicated to fostering growth, innovation, and measurable success.
</div>
""", unsafe_allow_html=True)

# --- TOOLS & TECHNOLOGIES ---
st.write("---")
st.header("🛠️ Tools & Technologies")
tools_html = """
<div style="text-align: left;">
    <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" />
    <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" />
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</div>
"""
st.markdown(tools_html, unsafe_allow_html=True)

# --- CORE EXPERTISE & RESUME ---
st.write("---")
col_left, col_right = st.columns(2)

with col_left:
    st.header("🎯 Core Expertise")
    st.write("🚀 **Product Management** | 🤖 **Process Automation**")
    st.write("📊 **Data Visualization** | 👥 **Team Leadership**")
    st.write("📈 **Capacity Planning** | 🧠 **Competitive Intel**")

with col_right:
    st.header("📄 Professional Resume")
    resume_file_name = "Nishant Ray - Resume.pdf"
    try:
        with open(resume_file_name, "rb") as file:
            st.download_button(label="📥 Download Resume (PDF)", data=file, file_name=resume_file_name, mime="application/pdf")
    except FileNotFoundError:
        st.error("Resume file not found.")

# --- CONTACT FORM (UPDATED EMAIL) ---
st.write("---")
st.header("📫 Get In Touch")
contact_form = f"""
<form action="https://formsubmit.co/raynishant09@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Message" required></textarea>
     <button type="submit" class="submit-btn">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
