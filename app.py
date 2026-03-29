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
    
    /* --- UPDATED PHOTO STYLING --- */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 12px; 
        overflow: hidden; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
        background-color: white; 
        padding: 5px;
        max-width: 320px; /* This controls the maximum size of the photo */
        margin: auto;
    }
    
    [data-testid="stImage"] img {
        display: block;
        width: 100%;
        height: auto;
    }

    /* Professional Blue Headers */
    h1, h2, h3 {
        color: #0e1117;
    }
    .main-text {
        font-size: 1.15rem;
        line-height: 1.7;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
# UPDATED: Changed column ratio to 0.8 and 3 to shrink the left side
col1, col2 = st.columns([0.8, 3], gap="large")

with col1:
    try:
        # UPDATED: Removed use_container_width to let the CSS max-width take over
        st.image("profile_pic.png")
    except:
        st.image("https://via.placeholder.com/220x280")

with col2:
    st.title("Hi, I'm Nishant Ray 👋")
    st.subheader("Seasoned Team Lead - Product | Automation Expert | Problem Solver")
    st.write("📍 Located in Gurugram, India")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nishant-ray-08222810a/)")

# --- ABOUT ME ---
st.write("---")
st.header("📌 About Me")
st.write(f"""
<div class="main-text">
As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over six years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions—empowering teams to automate processes, optimize workflows, and deliver impactful results.<br><br>
My expertise spans team management, capacity planning, and forecasting, complemented by a strong foundation in competitive intelligence, product management, data analytics, and data visualization.<br><br>
I am passionate about transforming complex challenges into clean, efficient code, enabling businesses to scale seamlessly and automate repetitive tasks. Driven by strategic thinking and a collaborative leadership style, I excel at aligning cross-functional teams with business objectives, ensuring projects are delivered on time and exceed expectations. Whether guiding product vision or architecting automation solutions, I am dedicated to fostering growth, innovation, and measurable success.
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
        st.write("- **Leadership:** Product Management, Team Leading, Capacity Planning")

with col_right:
    st.header("📄 Resume")
    st.info("Download my latest resume for a detailed look at my professional journey.")
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
        st.error(f"File '{resume_file_name}' not found on GitHub.")

# --- PROJECT GALLERY ---
st.write("---")
st.header("🚀 Featured Projects")
p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.image("https://images.pexels.com/photos/1036808/pexels-photo-1036808.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", caption="Automation Suite")
    with st.expander("View Details"):
        st.write("Built a Python automation suite that reduced manual entry time by 40%.")

with p_col2:
    st.image("https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", caption="Product Roadmap")
    with st.expander("View Details"):
        st.write("Led the lifecycle of a data-driven product from conception to launch.")

with p_col3:
    st.image("https://images.pexels.com/photos/1105389/pexels-photo-1105389.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", caption="Data Analytics Dashboard")
    with st.expander("View Details"):
        st.write("Developed a custom dashboard visualizing competitive intelligence and forecasting data.")

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
    st.write("Feel free to reach out for collaborations, leadership insights, or project discussions!")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
