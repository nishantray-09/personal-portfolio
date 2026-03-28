import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Professional Portfolio", page_icon="💼", layout="wide")

# 2. Advanced Styling (Fixing the previous error)
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Customizing the Profile Image */
    .profile-img {
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
    """, unsafe_allow_html=True) # Fixed parameter name here

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Use a real image path or a URL
    st.image("https://via.placeholder.com/250", width=250) 

with col2:
    st.title("Hi, I'm [Your Name] 👋")
    st.subheader("Software Engineer | Data Enthusiast | Problem Solver")
    st.write("📍 Located in [Your City, Country]")
    
    # LinkedIn Link
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yourprofile)")

# --- ABOUT ME ---
st.write("---")
st.header("📌 About Me")
st.write("""
<div class="main-text">
I am a driven professional with a background in <b>Python Development</b> and <b>Automation</b>. 
I specialize in creating clean, efficient code that helps businesses scale and automate 
repetitive tasks. When I'm not coding, you'll find me exploring new tech or contributing to open-source.
</div>
""", unsafe_allow_html=True)

# --- SKILLS & RESUME ---
st.write("---")
col_left, col_right = st.columns(2)

with col_left:
    st.header("🛠️ Technical Skills")
    # Using columns inside columns for a clean grid
    skill_col1, skill_col2 = st.columns(2)
    with skill_col1:
        st.write("- **Languages:** Python, SQL, C++")
        st.write("- **Frameworks:** Streamlit, Flask, Django")
    with skill_col2:
        st.write("- **Cloud:** AWS, Docker, Git")
        st.write("- **Data:** Pandas, NumPy, Matplotlib")

with col_right:
    st.header("📄 Resume")
    st.info("Download my latest resume for a detailed look at my experience.")
    # Note: Ensure "resume.pdf" exists in your folder
    try:
        with open("resume.pdf", "rb") as file:
            st.download_button(
                label="📥 Download Resume (PDF)",
                data=file,
                file_name="My_Professional_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Resume file not found. Please add 'resume.pdf' to your project folder.")

# --- PROJECT GALLERY (The 'Fancy' Part) ---
st.write("---")
st.header("🚀 Featured Projects")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.image("https://via.placeholder.com/300x200", caption="Automation Suite")
    with st.expander("View Details"):
        st.write("Built a Python automation suite that reduced manual entry time by 40%.")

with p_col2:
    st.image("https://via.placeholder.com/300x200", caption="Data Dashboard")
    with st.expander("View Details"):
        st.write("Interactive dashboard visualizing real-time sales data using Streamlit.")

with p_col3:
    st.image("https://via.placeholder.com/300x200", caption="API Integration")
    with st.expander("View Details"):
        st.write("Developed a custom REST API to connect legacy systems with modern apps.")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 [Your Name] | Built with Python & Streamlit")