import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Nishant Ray | Portfolio", page_icon="💼", layout="wide")

# 2. Advanced Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    [data-testid="stImage"] img {
        border-radius: 50%;
        border: 4px solid #0077b5;
    }
    h1, h2 {
        color: #0e1117;
    }
    .main-text {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    try:
        st.image("profile_pic.png", width=250)
    except:
        st.image("https://via.placeholder.com/250", width=250)

with col2:
    st.title("Hi, I'm Nishant Ray 👋")
    st.subheader("Team Lead - Product | Data Enthusiast | Problem Solver")
    st.write("📍 Located in Gurugram, India")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nishant-ray-08222810a/)")

# --- ABOUT ME ---
st.write("---")
st.header("📌 About Me")
st.write("""
<div class="main-text">
I am a driven professional with a background in <b>Python Development</b> and <b>Automation</b>. 
As a Team Lead, I specialize in bridging the gap between product vision and technical execution, 
creating clean, efficient code that helps businesses scale and automate repetitive tasks.
</div>
""", unsafe_allow_html=True)

# --- SKILLS & RESUME ---
st.write("---")
col_left, col_right = st.columns(2)

with col_left:
    st.header("🛠️ Technical Skills")
    skill_col1, skill_col2 = st.columns(2)
    with skill_col1:
        st.write("- **Languages:** Python, SQL, C++")
        st.write("- **Frameworks:** Streamlit, Flask, Django")
    with skill_col2:
        st.write("- **Cloud:** AWS, Docker, Git")
        st.write("- **Leadership:** Product Management, Team Leading")

with col_right:
    st.header("📄 Resume")
    st.info("Download my latest resume for a detailed look at my professional journey.")
    
    # UPDATED: Matching your specific filename
    resume_file_name = "Nishant Ray - Resume.pdf"
    
    try:
        with open(resume_file_name, "rb") as file:
            st.download_button(
                label="📥 Download Resume (PDF)",
                data=file,
                file_name=resume_file_name,
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error(f"File '{resume_file_name}' not found. Please ensure it is uploaded to GitHub exactly as named.")

# --- PROJECT GALLERY ---
st.write("---")
st.header("🚀 Featured Projects")
p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.image("https://via.placeholder.com/300x200", caption="Automation Suite")
    with st.expander("View Details"):
        st.write("Built a Python automation suite that reduced manual entry time by 40%.")

with p_col2:
    st.image("https://via.placeholder.com/300x200", caption="Product Roadmap")
    with st.expander("View Details"):
        st.write("Led the lifecycle of a data-driven product from conception to launch.")

with p_col3:
    st.image("https://via.placeholder.com/300x200", caption="API Integration")
    with st.expander("View Details"):
        st.write("Developed custom REST APIs to streamline internal data sharing.")

# --- CONTACT FORM ---
st.write("---")
st.header("📫 Get In Touch With Me!")

# Reminder: Replace 'your-email@example.com' with your real email
contact_form = """
<form action="https://formsubmit.co/your-email@example.com" method="POST">
     <input type="hidden" name="_tracker" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
     <textarea name="message" placeholder="Your Message Here" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 100px;"></textarea>
     <button type="submit" style="background-color: #0077b5; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
</form>
"""

c_col1, c_col2 = st.columns(2)
with c_col1:
    st.markdown(contact_form, unsafe_allow_html=True)
with c_col2:
    st.write("###")
    st.write("Feel free to reach out for collaborations or project discussions!")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
