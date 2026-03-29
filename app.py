import streamlit as st
import streamlit_analytics2 as analytics # 1. Import the library

# 2. Wrap EVERYTHING in this 'with' block
with analytics.track():
    
    # --- ALL YOUR EXISTING CODE STARTS HERE ---
    st.set_page_config(page_title="Nishant Ray | Product Leader", page_icon="💼", layout="wide")

    # --- SUCCESS MESSAGE LOGIC ---
    query_params = st.query_params
    if query_params.get("sent") == "true":
        st.success("✅ Thank you for reaching out! I've received your message and will get back to you soon.")

    # 2. Advanced Styling
    st.markdown("""
        <style>
        .stApp { 
            background: linear-gradient(-45deg, #0a192f, #0d1f3d, #0a192f);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .pronouns { font-size: 1.2rem; color: #8892b0; font-weight: 400; margin-left: 10px; }
        .contact-subtext { color: #64ffda; font-size: 1rem; margin-top: 5px; font-family: 'Courier New', monospace; background: rgba(100, 255, 218, 0.05); padding: 5px 15px; border-radius: 5px; display: inline-block; }
        .summary-text { font-size: 1.15rem; line-height: 1.6; color: #8892b0; }
        [data-testid="stImage"] { border-radius: 15px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); max-width: 280px; margin: auto; border: 2px solid #172a45; }
        .linkedin-container { margin-top: 20px; }
        .social-icon { width: 35px; transition: all 0.3s ease-in-out; filter: brightness(0) invert(1) drop-shadow(0px 0px 1px #64ffda); }
        .social-icon:hover { transform: translateY(-3px); filter: brightness(0) invert(1) drop-shadow(0px 0px 8px #64ffda); }
        h1, h2, h3 { color: #ccd6f6 !important; font-weight: 700; }
        .contact-form-container { max-width: 500px; margin-left: 0; text-align: left; }
        input, textarea { background-color: #172a45 !important; color: #ccd6f6 !important; border: 1px solid #233554 !important; border-radius: 8px !important; padding: 10px !important; width: 100% !important; margin-bottom: 10px !important; }
        .submit-btn { background-color: transparent; color: #64ffda; padding: 10px 20px; border: 1px solid #64ffda; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold; transition: 0.3s; }
        .submit-btn:hover { background-color: rgba(100, 255, 218, 0.1); box-shadow: 0 0 10px #64ffda; }
        hr { border: 0; height: 1px; background: #233554; }
        </style>
        """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 3], gap="large")
    with col1:
        try: st.image("profile_pic.png")
        except: st.image("https://via.placeholder.com/280x350")
    with col2:
        st.markdown(f'<h1>Nishant Ray <span class="pronouns">(He/Him)</span></h1>', unsafe_allow_html=True)
        st.subheader("Product Team Lead | Automation Architect | Strategy & Execution")
        st.markdown("""<div class="contact-subtext">📧 raynishant09@gmail.com &nbsp;|&nbsp; 📱 +91 9481955387 &nbsp;|&nbsp; 📍 Gurugram, India</div>""", unsafe_allow_html=True)
        st.markdown("""<div class="linkedin-container"><a href="https://www.linkedin.com/in/nishant-ray-08222810a/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" class="social-icon"></a></div>""", unsafe_allow_html=True)

    # --- SUMMARY ---
    st.write("---")
    st.header("📌 Summary")
    st.write('<div class="summary-text"><p>As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution...</p></div>', unsafe_allow_html=True)

    # --- TOOLS & TECHNOLOGIES ---
    st.write("---")
    st.header("🛠️ Tools & Technologies")
    st.markdown("""<div style="text-align: left;"><img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" /></div>""", unsafe_allow_html=True)

    # --- CORE EXPERTISE & RESUME ---
    st.write("---")
    col_left, col_right = st.columns(2)
    with col_left:
        st.header("🎯 Core Expertise")
        st.write("🚀 **Product Management** | 🤖 **Process Automation** | 📊 **Data Visualization** | 👥 **Team Leadership**")
    with col_right:
        st.header("📄 Resume")
        try:
            with open("Nishant Ray - Resume.pdf", "rb") as file:
                st.download_button(label="📥 DOWNLOAD CV (PDF)", data=file.read(), file_name="Nishant Ray - Resume.pdf", mime="application/pdf")
        except: st.error("Resume file not found.")

    # --- CONTACT FORM ---
    st.write("---")
    st.header("📫 Get In Touch")
    contact_form = f"""<div class="contact-form-container"><form action="https://formsubmit.co/raynishant09@gmail.com" method="POST"><input type="hidden" name="_next" value="https://nishant-portfolio.streamlit.app/?sent=true"><input type="text" name="name" placeholder="Name" required><input type="email" name="email" placeholder="Email" required><textarea name="message" placeholder="Message" required style="height: 80px;"></textarea><button type="submit" class="submit-btn">Send Message</button></form></div>"""
    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("---")
    st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
