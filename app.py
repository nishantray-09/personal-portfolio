import streamlit as st
import streamlit_analytics2 as analytics 

# Wrap everything in the analytics tracker
with analytics.track():
    
    # 1. Page Configuration
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
        .summary-text p { margin-bottom: 12px !important; }
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
        
        /* --- CORE EXPERTISE BADGES --- */
        .expert-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 12px;
            margin-top: 15px;
        }
        .expert-badge {
            background-color: rgba(23, 42, 69, 0.7);
            border: 1px solid #233554;
            color: #ccd6f6;
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
        }
        .expert-badge:hover {
            border-color: #64ffda;
            color: #64ffda;
            transform: translateX(3px);
        }
        .expert-badge span {
            margin-right: 8px;
            font-size: 1.1rem;
        }

        /* --- RECOMMENDATIONS & PROJECTS CARD STYLING --- */
        .rec-card, .project-card {
            background-color: #172a45;
            border: 1px solid #233554;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .rec-card:hover, .project-card:hover {
            transform: translateY(-5px);
            border-color: #64ffda;
        }
        .rec-text, .project-desc {
            color: #8892b0;
            font-size: 1.02rem;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        .rec-text { font-style: italic; }
        .rec-author, .project-title {
            color: #ccd6f6;
            font-weight: 600;
            font-size: 1.2rem;
            margin-bottom: 2px;
        }
        .project-meta {
            color: #64ffda;
            font-size: 0.85rem;
            font-family: 'Courier New', monospace;
            margin-bottom: 12px;
        }
        .rec-title {
            color: #64ffda;
            font-size: 0.85rem;
            font-family: 'Courier New', monospace;
            line-height: 1.3;
        }
        .metric-highlight {
            background: rgba(100, 255, 218, 0.1);
            color: #64ffda;
            padding: 6px 12px;
            border-radius: 6px;
            font-weight: 600;
            display: inline-block;
            margin-top: 10px;
            border: 1px dashed rgba(100, 255, 218, 0.3);
        }
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

    st.write("---")

    # --- TABS FOR NAVIGATION ---
    tab_about, tab_projects, tab_recommendations = st.tabs(["👤 About Me", "🚀 Projects", "💬 LinkedIn Recommendations"])

    # ==================== TAB 1: ABOUT ME ====================
    with tab_about:
        # --- FULL SUMMARY RESTORED ---
        st.header("📌 Summary")
        st.markdown("""
        <div class="summary-text">
        <p>As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over seven years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions—empowering teams to automate processes, optimize workflows, and deliver impactful results.</p>
        <p>My expertise spans team management, capacity planning, and forecasting, complemented by a strong foundation in competitive intelligence, product management, data analytics, and data visualization.</p>
        <p>I am passionate about transforming complex challenges into clean, efficient code, enabling businesses to scale seamlessly and automate repetitive tasks. Driven by strategic thinking and a collaborative leadership style, I excel at aligning cross-functional teams with business objectives, ensuring projects are delivered on time and exceed expectations. Whether guiding product vision or architecting automation solutions, I am dedicated to fostering growth, innovation, and measurable success.</p>
        </div>
        """, unsafe_allow_html=True)

        # --- TOOLS & TECHNOLOGIES ---
        st.write("---")
        st.header("🛠️ Tools & Technologies")
        st.markdown("""<div style="text-align: left;"><img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" /></div>""", unsafe_allow_html=True)

        # --- CORE EXPERTISE & RESUME ---
        st.write("---")
        col_left, col_right = st.columns(2)
        with col_left:
            st.header("🎯 Core Expertise")
            st.markdown("""
            <div class="expert-grid">
                <div class="expert-badge"><span>🤖</span> Automation</div>
                <div class="expert-badge"><span>🧠</span> Machine Learning</div>
                <div class="expert-badge"><span>🌐</span> Software Product Management</div>
                <div class="expert-badge"><span>📊</span> Business Data Management</div>
                <div class="expert-badge"><span>⚙️</span> Product Operations</div>
                <div class="expert-badge"><span>🚀</span> Product Management</div>
                <div class="expert-badge"><span>📈</span> Data Visualization</div>
                <div class="expert-badge"><span>👥</span> Team Leadership</div>
                <div class="expert-badge"><span>📅</span> Capacity Planning</div>
                <div class="expert-badge"><span>🔍</span> Competitive Intel</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col_right:
            st.header("📄 Resume")
            try:
                with open("Nishant Ray - Resume.pdf", "rb") as file:
                    st.download_button(label="📥 DOWNLOAD CV (PDF)", data=file.read(), file_name="Nishant Ray - Resume.pdf", mime="application/pdf")
            except: st.error("Resume file not found.")

    # ==================== TAB 2: PROJECTS ====================
    with tab_projects:
        st.header("📂 Featured Projects")
        st.write("A showcase of key automation frameworks, analytical tools, and product initiatives built to drive business efficiency.")
        st.write("")

        # Project Card 1: CRM Lead Ingestion Automation
        st.markdown("""
        <div class="project-card">
            <div class="project-title">💼 CRM Lead Ingestion Automation</div>
            <div class="project-meta">Mar 2026 – Apr 2026 &nbsp;|&nbsp; Associated with G2</div>
            <div class="project-desc">
                Integrated AI frameworks and Python architecture to build an end-to-end automated scraping engine. 
                The solution targets inbox ecosystems to extract inbound email leads, parse unstructured data, and dynamically route parsed, high-intent lead attributes onto the centralized CRM platform.
            </div>
            <div style="margin-bottom: 15px;">
                <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
                <img src="https://img.shields.io/badge/Google_Gemini-8E75FF?style=flat&logo=googlegemini&logoColor=white" />
            </div>
            <div class="metric-highlight">⏱️ Impact: Saved ~80 hours/month with 100% data accuracy</div>
        </div>
        """, unsafe_allow_html=True)

        # Project Card 2: Gen AI Dashboard
        st.markdown("""
        <div class="project-card">
            <div class="project-title">📊 Gen AI Dashboard</div>
            <div class="project-meta">Mar 2024 – Apr 2024 &nbsp;|&nbsp; Associated with Gartner</div>
            <div class="project-desc">
                Designed and implemented a dynamic data monitoring workspace to track evolving Generative AI data trends. 
                By combining warehouse data processing with visualization layers, this dashboard empowers leadership teams with real-time, actionable macro-level insights while streamlining deep operational reporting processes.
            </div>
            <div style="margin-bottom: 15px;">
                <img src="https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=microsoftpowerbi&logoColor=black" />
                <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white" />
            </div>
            <div class="metric-highlight">⏱️ Impact: Saved ~30 hours/month through streamlined reporting processes</div>
        </div>
        """, unsafe_allow_html=True)

    # ==================== TAB 3: RECOMMENDATIONS ====================
    with tab_recommendations:
        st.header("💬 Recommendations")
        st.write("Testimonials from managers, colleagues, and team members received on LinkedIn.")
        st.write("")

        rec_col1, rec_col2 = st.columns(2, gap="large")

        with rec_col1:
            # 1. Laxmi Narasimhan Akshay
            st.markdown("""
            <div class="rec-card">
                <div class="rec-text">"Lots of people talk about self learning and up-skilling as one of their key pursuits in their career, very few walk the talk. Nishant goes above and beyond in putting it into practice, you give him a problem and structure to approach and he goes out and figures out the rest. Even if it means learning skills as intensive as SQL, Power BI, Power Apps etc. from scratch. And once he is committed, you rarely need to follow up as he would be on your case to share progress, roadblocks and potential workaround he is already trying to figure. Very rarely you get across people with such high levels of motivation and self drive. Can't recommend him enough to any potential employer."</div>
                <div class="rec-author">Laxmi Narasimhan Akshay</div>
                <div class="rec-title">Senior Product Leader @ Gartner | ISB Alumnus</div>
            </div>
            """, unsafe_allow_html=True)
            
            # 2. Bhargava Bhavaraju
            st.markdown("""
            <div class="rec-card">
                <div class="rec-text">
                    "I had the opportunity to work with Nishant, and it was genuinely a great learning experience. Nishant has a strong ability to balance strategic thinking with execution, especially in areas like automation, analytics, and operational management.<br><br>
                    What stood out most to me was his approach to leadership. He was always approachable, solution-oriented, and deeply involved in helping the team grow while ensuring business goals were met efficiently. His ability to identify bottlenecks, streamline workflows, and drive impactful improvements consistently created a positive impact across projects and team operations.<br><br>
                    Beyond his technical and analytical expertise, Nishant brings a collaborative and supportive leadership style that makes working with him both productive and motivating. I’m confident he will continue to create significant value wherever he goes, and I would highly recommend him to any organization."
                </div>
                <div class="rec-author">Bhargava Bhavaraju</div>
                <div class="rec-title">Product Reviews Associate @ G2 | Ex-Gartner</div>
            </div>
            """, unsafe_allow_html=True)

            # 3. Mahima Kapoor
            st.markdown("""
            <div class="rec-card">
                <div class="rec-text">"Nishant has been a star performer and the easiest colleague to work with. His exceptional communication skills and commitments towards works makes him stand out of the crowd. His honesty, mindfulness and innovative thinking are the greatest assets."</div>
                <div class="rec-author">Mahima Kapoor</div>
                <div class="rec-title">Consultant at Accenture | Ex-Google (Operations) | Ex-Gartner</div>
            </div>
            """, unsafe_allow_html=True)

        with rec_col2:
            # 4. Garima Kalra
            st.markdown("""
            <div class="rec-card">
                <div class="rec-text">"Nishant excels in all areas of his role especially project management, building dashboarding, and audit. He often goes and beyond to deliver high-quality results. He is known for his problem-solving abilities, and teamwork which significantly contributes to our team's success. He approaches every project with enthusiasm and dedication.<br><br>In addition to his professional skills, Nishant is a pleasure to work with. He is supportive of colleagues, communicates effectively, and fosters a collaborative and positive work environment."</div>
                <div class="rec-author">Garima Kalra</div>
                <div class="rec-title">Senior Manager, G2 India | Ex-Gartner | Ex-E&Y</div>
            </div>
            """, unsafe_allow_html=True)

            # 5. Alka Gupta
            st.markdown("""
            <div class="rec-card">
                <div class="rec-text">"Nishant and I worked together on multiple high impact projects in the same team. He is an amazing co-worker, extremely humble, disciplined and has a knack for learning new things continuously. His analytically driven approach has helped me explore new dimensions at work and he will be a great asset to any workplace."</div>
                <div class="rec-author">Alka Gupta</div>
                <div class="rec-title">Data Analytics Engineer | Ex-Amazon</div>
            </div>
            """, unsafe_allow_html=True)

    # --- CONTACT FORM ---
    st.write("---")
    st.header("📫 Get In Touch")
    my_website_url = "https://nishant-portfolio.streamlit.app" 
    contact_form = f"""<div class="contact-form-container"><form action="https://formsubmit.co/raynishant09@gmail.com" method="POST"><input type="hidden" name="_next" value="{my_website_url}/?sent=true"><input type="hidden" name="_subject" value="New Portfolio Inquiry"><input type="hidden" name="_captcha" value="false"><input type="text" name="name" placeholder="Name" required><input type="email" name="email" placeholder="Email" required><textarea name="message" placeholder="Message" required style="height: 80px;"></textarea><button type="submit" class="submit-btn">Send Message</button></form></div>"""
    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("---")
    st.caption("© 2026 Nishant Ray | Built with Python & Streamlit")
