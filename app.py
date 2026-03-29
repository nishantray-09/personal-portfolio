import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Nishant Ray | Product Leader", page_icon="💼", layout="wide")

# 2. Advanced Styling
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; }
    [data-testid="stImage"] {
        border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); 
        max-width: 280px; 
        margin: auto;
        border: 1px solid #30363d;
    }
    .main-text { font-size: 1.15rem; line-height: 1.8; color: #c9d1d9; }
    h1, h2, h3 { color: #ffffff !important; }
    
    /* Tool Badge Styling */
    .tool-badge {
        display: inline-block;
        padding: 5px 12px;
        margin: 5px;
        border-radius: 20px;
        background-color: #1c2128;
        border: 1px solid #30363d;
        color: #00a0dc;
        font-weight: bold;
        font-size: 0.9rem;
    }
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
    st.subheader("Product Team Lead | Automation Architect | Strategy & Execution")
    st.write("📍 Gurugram, India")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nishant-ray-08222810a/)")

# --- ABOUT ME ---
st.write("---")
st.header("📌 Executive Summary")
st.write(f"""
<div class="main-text">
As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over six years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions...
</div>
""", unsafe_allow_html=True)

# --- NEW TOOLS SECTION ---
st.write("---")
st.header("🛠️ Tools & Technologies")

# Creating a visually appealing grid of tech badges
# We use markdown with shields.io for a "Pro" developer look
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

# --- SKILLS & RESUME ---
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

# --- CONTACT FORM ---
st.write("---")
st.header("📫 Get In Touch")
contact_form = """
<form action="https://formsubmit.co/your-email@example.com" method="POST">
     <input type="text" name="name" placeholder="Name" required style="width: 100%; padding: 12px; margin-bottom: 12px; background-color: #1c2128; color: white; border: 1px solid #30363d;">
     <input type="email" name="email" placeholder="Email" required style="width: 100%; padding: 12px; margin-bottom: 12px; background-color: #1c2128; color: white; border: 1px solid #30363d;">
     <textarea name="message" placeholder="Message" required style="width: 100%; padding: 12px; margin-bottom: 12px; height: 100px; background-color: #1c2128; color: white; border: 1px solid #30363d;"></textarea>
     <button type="submit" style="background-color: #00a0dc; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; width: 100%;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
