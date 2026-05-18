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

    # 2. Premium Professional UI Styling
    st.markdown("""
        <style>
        /* Living Dynamic Gradient Background */
        .stApp { 
            background: linear-gradient(-45deg, #020c1b, #0a192f, #0f2b48, #0a192f);
            background-size: 400% 400%;
            animation: slowGradient 25s ease infinite;
        }
        @keyframes slowGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Smooth Fade-In Animation for Content */
        .fade-in {
            animation: fadeInPage 1.2s ease-out forwards;
        }
        @keyframes fadeInPage {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .pronouns { font-size: 1.2rem; color: #8892b0; font-weight: 400; margin-left: 10px; }
        .contact-subtext { color: #64ffda; font-size: 1rem; margin-top: 5px; font-family: 'Courier New', monospace; background: rgba(100, 255, 218, 0.05); padding: 5px 15px; border-radius: 5px; display: inline-block; }
        .summary-text { font-size: 1.15rem; line-height: 1.6; color: #8892b0; }
        .summary-text p { margin-bottom: 12px !important; }
        
        [data-testid="stImage"] { border-radius: 15px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6); max-width: 280px; margin: auto; border: 2px solid #233554; transition: all 0.4s ease; }
        [data-testid="stImage"]:hover { transform: scale(1.02); border-color: #64ffda; box-shadow: 0 15px 35px rgba(100, 255, 218, 0.15); }
        
        .social-container { margin-top: 20px; display: flex; gap: 15px; }
        .social-icon { width: 35px; transition: all 0.3s ease-in-out; filter: brightness(0) invert(1) drop-shadow(0px 0px 1px #64ffda); }
        .social-icon:hover { transform: translateY(-4px); filter: brightness(0) invert(1) drop-shadow(0px 0px 10px #64ffda); }
        h1, h2, h3 { color: #ccd6f6 !important; font-weight: 700; }
        
        /* Custom Native Streamlit Metric Overrides for Dark Mode */
        [data-testid="stMetricValue"] { color: #64ffda !important; font-family: 'Courier New', monospace; font-weight: 700 !important; }
        [data-testid="stMetricLabel"] { color: #ccd6f6 !important; font-size: 1rem !important; }
        [data-testid="stMetricDelta"] { color: #8892b0 !important; }

        .contact-form-container { max-width: 500px; margin-left: 0; text-align: left; }
        input, textarea { background-color: #172a45 !important; color: #ccd6f6 !important; border: 1px solid #233554 !important; border-radius: 8px !important; padding: 10px !important; width: 100% !important; margin-bottom: 10px !important; }
        .submit-btn { background-color: transparent; color: #64ffda; padding: 10px 20px; border: 1px solid #64ffda; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold; transition: 0.3s; }
        .submit-btn:hover { background-color: rgba(100, 255, 218, 0.1); box-shadow: 0 0 10px #64ffda; }
        hr { border: 0; height: 1px; background: #233554; }
        
        /* --- CORE EXPERTISE BLOCK STRUCTURE --- */
        .expert-section {
            background-color: #172a45;
            border: 1px solid #233554;
            padding: 22px;
            border-radius: 12px;
            margin-top: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            transition: border-color 0.3s ease;
        }
        .expert-section:hover {
            border-color: #64ffda;
        }
        .expert-list { list-style-type: none; padding-left: 0; color: #8892b0; font-size: 1.05rem; margin-bottom: 0; }
        .expert-list li { margin-bottom: 12px; display: flex; align-items: center; }
        .expert-list li:last-child { margin-bottom: 0; }
        .expert-list li::before { content: "▹"; color: #64ffda; margin-right: 12px; font-weight: bold; font-size: 1.1rem; }

        /* --- CARD GLOW MICRO-INTERACTIONS --- */
        .rec-card, .project-card {
            background-color: #172a45;
            border: 1px solid #233554;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        .rec-card:hover, .project-card:hover {
            transform: translateY(-6px);
            border-color: #64ffda;
            box-shadow: 0 15px 30px rgba(100, 255, 218, 0.08);
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
            background: rgba(100, 255, 218, 0.08);
            color: #64ffda;
            padding: 8px 14px;
            border-radius: 6px;
            font-weight: 600;
            display: inline-block;
            margin-top: 10px;
            border: 1px dashed rgba(100, 255, 218, 0.3);
            font-family: 'Courier New', monospace;
        }
        </style>
        """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3], gap="large")
    with col1:
        try: st.image("profile_pic.png")
        except: st.image("https://via.placeholder.com/280x350")
    with col2:
        st.markdown(f'<h1>Nishant Ray <span class="pronouns">(He/Him)</span></h1>', unsafe_allow_html=True)
        st.subheader("Product Lead | Automation Architect | Strategy & Operations")
        st.markdown("""<div class="contact-subtext">📧 raynishant09@gmail.com &nbsp;|&nbsp; 📱 +91 9481955387 &nbsp;|&nbsp; 📍 Gurugram, India</div>""", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="social-container">
            <a href="https://www.linkedin.com/in/nishant-ray-08222810a/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" class="social-icon">
            </a>
            <a href="https://github.com/nishantray-09" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" class="social-icon">
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # --- TABS FOR NAVIGATION ---
    tab_about, tab_projects, tab_recommendations = st.tabs(["👤 Executive Summary", "🚀 Impact Case Studies", "💬 Professional Testimonials"])

    # ==================== TAB 1: EXECUTIVE SUMMARY ====================
    with tab_about:
        # --- EXECUTIVE IMPACT TICKER ---
        st.write("")
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        with m_col1:
            st.metric(label="🔥 Operational Efficiency", value="110+ Hours", delta="Saved Monthly")
        with m_col2:
            st.metric(label="🎯 Automation Precision", value="100%", delta="Lead Data Accuracy")
        with m_col3:
            st.metric(label="🧠 Cross-Functional Experience", value="7+ Years", delta="Tech & Strategy Matrix")
        with m_col4:
            st.metric(label="👥 Leadership Footprint", value="Team Lead", delta="Enterprise Scale Assets")
        
        st.write("---")
        
        st.header("📌 Professional Summary")
        st.markdown("""
        <div class="summary-text">
        <p>As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over seven years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions—empowering teams to automate processes, optimize workflows, and deliver impactful results.</p>
        <p>My expertise spans team management, capacity planning, and forecasting, complemented by a strong foundation in competitive intelligence, product management, data analytics, and data visualization.</p>
        <p>I am passionate about transforming complex challenges into clean, efficient code, enabling businesses to scale seamlessly and automate repetitive tasks. Driven by strategic thinking and a collaborative leadership style, I excel at aligning cross-functional teams with business objectives, ensuring projects are delivered on time and exceed expectations.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("---")
        st.header("🛠️ Tech Stack Core")
        st.markdown("""<div style="text-align: left;"><img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black" /> <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" /></div>""", unsafe_allow_html=True)

        st.write("---")
        col_left, col_right = st.columns(2)
        with col_left:
            st.header("🎯 Core Pillars of Expertise")
            
            p1, p2 = st.columns(2)
            with p1:
                st.markdown('<div class="expert-section">', unsafe_allow_html=True)
                st.markdown("##### 🌐 Product Strategy")
                st.markdown("""<ul class="expert-list"><li>Software Product Management</li><li>Product Operations</li><li>Competitive Intelligence</li><li>Team Leadership</li></ul>""", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            with p2:
                st.markdown('<div class="expert-section">', unsafe_allow_html=True)
                st.markdown("##### 📊 Automation & Data")
                st.markdown("""<ul class="expert-list"><li>Intelligent Automation</li><li>Machine Learning Models</li><li>Business Data Management</li><li>Capacity Planning & Forecasting</li></ul>""", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
        with col_right:
            st.header("📄 Executive Resume")
            st.write("Review my formal trajectory, credential architecture, and organizational progression details.")
            st.write("")
            try:
                with open("Nishant Ray - Resume.pdf", "rb") as file:
                    st.download_button(label="📥 DOWNLOAD CV (PDF ARCHIVE)", data=file.read(), file_name="Nishant Ray - Resume.pdf", mime="application/pdf")
            except: st.error("Resume document matrix file not discovered locally.")

    # ==================== TAB 2: IMPACT CASE STUDIES ====================
    with tab_projects:
        st.header("📂 Strategic Initiatives & Systems Architecture")
        st.write("A deep dive into architectural frameworks engineered to eliminate overhead and drive programmatic data clarity.")
        st.write("")

        # Case Study 1
        st.markdown("""
        <div class="project-card">
            <div class="project-title">💼 CRM Lead Ingestion Automation Engine</div>
            <div class="project-meta">Mar 2026 – Apr 2026 &nbsp;|&nbsp; Enterprise System @ G2</div>
            <div class="project-desc">
                Integrated artificial intelligence protocols with Python runtime frameworks to structure an end-to-end extraction utility. 
                The software hooks inbound mail distributions, systematically dissects schema-less unstructured payloads, isolates operational customer parameters, and pipelines ingestion fields onto the enterprise CRM architecture.
            </div>
            <div style="margin-bottom: 15px;">
                <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
                <img src="https://img.shields.io/badge/Google_Gemini-8E75FF?style=flat&logo=googlegemini&logoColor=white" />
            </div>
            <div class="metric-highlight">📊 Metrics: Conserved ~80 Engineering-Hours/Month @ 100% Data Integrity</div>
        </div>
        """, unsafe_allow_html=True)

        # Case Study 2
        st.markdown("""
        <div class="project-card">
            <div class="project-title">📊 Analytics Framework: Gen AI Corporate Dashboard</div>
            <div class="project-meta">Mar 2024 – Apr 2024 &nbsp;|&nbsp; Business Intelligence Unit @ Gartner</div>
            <div class="project-desc">
                Architected and deployed a multi-tier pipeline optimization workspace designed to visualize fluctuating global Generative AI technology trends. 
                The delivery involved setting warehouse telemetry aggregations beneath robust dashboarding visual control interfaces, enabling executives with proactive data discoveries while shortening data cycle times.
            </div>
            <div style="margin-bottom: 15px;">
                <img src="https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=microsoftpowerbi&logoColor=black" />
                <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white" />
            </div>
            <div class="metric-highlight">📊 Metrics: Trimmed Reporting Overheads by ~30 Hours Monthly via Data Consolidation</div>
        </div>
        """, unsafe_allow_html=True)

    # ==================== TAB 3: PROFESSIONAL TESTIMONIALS ====================
    with tab_recommendations:
        st.header("💬 Verified Stakeholder Recommendations")
        st.write("Direct endorsements and recommendations logged via professional peers and enterprise leadership on LinkedIn.")
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
    st.header("📫 Connection Portal")
    my_website_url = "https://nishant-portfolio.streamlit.app" 
    contact_form = f"""<div class="contact-form-container"><form action="https://formsubmit.co/raynishant09@gmail.com" method="POST"><input type="hidden" name="_next" value="{my_website_url}/?sent=true"><input type="hidden" name="_subject" value="New Portfolio Inquiry"><input type="hidden" name="_captcha" value="false"><input type="text" name="name" placeholder="Name" required><input type="email" name="email" placeholder="Email" required><textarea name="message" placeholder="Message" required style="height: 80px;"></textarea><button type="submit" class="submit-btn">Send Message</button></form></div>"""
    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("---")
    st.caption("© 2026 Nishant Ray | Engineered with Python & Streamlit Core")
    st.markdown('</div>', unsafe_allow_html=True)
