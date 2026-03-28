import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Nishant Ray | Portfolio", page_icon="💼", layout="wide")

# 2. Advanced Styling
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Customizing the Profile Image to be circular */
    [data-testid="stImage"] img {
        border-radius: 50%;
        border: 4px solid #0077b5;
    }
    /* Professional Blue Headers */
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
    # UPDATED: Using your uploaded profile pic
    # Note: Ensure the file extension is correct (e.g., .jpg, .png)
    st.image("profile_pic.png", width=250) 

with col2:
    st.title("Hi, I'm Nishant Ray 👋")
    st.subheader("Team Lead - Product | Data Enthusiast | Problem Solver")
    st.write("📍 Located in Gurugram, India")
    
    # UPDATED: Your specific LinkedIn Link
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
    try:
        with open("resume.pdf", "rb") as file:
            st.download_button(
                label="📥 Download Resume (PDF)",
                data=file,
                file_name="Nishant_Ray_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Resume file not found. Ensure 'resume.pdf' is uploaded to your GitHub repository.")

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

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
