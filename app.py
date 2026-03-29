import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Nishant Ray | Product Leader", page_icon="💼", layout="wide")

# 2. Advanced Styling for Dark/Authoritative Theme
st.markdown("""
    <style>
    /* Global Background Fix */
    .stApp {
        background-color: #0b0e14;
    }

    /* Professional Profile Photo Frame */
    [data-testid="stImage"] {
        border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); 
        max-width: 280px; 
        margin: auto;
        border: 1px solid #30363d;
    }
    
    /* Contact Form Styling for Dark Theme */
    input, textarea {
        background-color: #1c2128 !important;
        color: #ecf0f1 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    
    /* Headers & Text */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700;
    }
    .main-text {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #c9d1d9;
    }

    /* Customizing the Divider Line */
    hr {
        border: 0;
        height: 1px;
        background: #30363d;
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
As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over six years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions—empowering teams to automate processes, optimize workflows, and deliver impactful results.<br><br>
My expertise spans team management, capacity planning, and forecasting, complemented by a strong foundation in competitive intelligence, product management, data analytics, and data visualization.<br><br>
I am passionate about transforming complex challenges into clean, efficient code, enabling businesses to scale seamlessly and automate repetitive tasks. Driven by strategic thinking and a collaborative leadership style, I excel at aligning cross-functional teams with business objectives, ensuring projects are delivered on time and exceed expectations.
</div>
""", unsafe_allow_html=True)

# --- SKILLS & RESUME ---
st.write("---")
col_left, col_right = st.columns(2)

with col_left:
    st.header("🛠️ Core Expertise")
    skill_col1, skill_col2 = st.columns(2)
    with skill_col1:
        st.write("🚀 **Product Management**")
        st.write("🤖 **Process Automation**")
        st.write("📊 **Data Visualization**")
    with skill_col2:
        st.write("👥 **Team Leadership**")
        st.write("📈 **Capacity Planning**")
        st.write("🧠 **Competitive Intel**")

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
st.header("📫 Contact")

# REPLACE WITH YOUR REAL EMAIL
contact_form = """
<form action="https://formsubmit.co/your-email@example.com" method="POST">
     <input type="text" name="name" placeholder="Name" required style="width: 100%; padding: 12px; margin-bottom: 12px;">
     <input type="email" name="email" placeholder="Email" required style="width: 100%; padding: 12px; margin-bottom: 12px;">
     <textarea name="message" placeholder="Message" required style="width: 100%; padding: 12px; margin-bottom: 12px; height: 100px;"></textarea>
     <button type="submit" style="background-color: #00a0dc; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; width: 100%;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
