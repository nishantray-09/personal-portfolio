# 2. Advanced Styling (Updated for tighter paragraph spacing)
st.markdown("""
    <style>
    .stApp { background-color: #0a192f; }
    
    /* Targets the specific about-me text container */
    .summary-text {
        font-size: 1.15rem;
        line-height: 1.6; /* Reduced line height slightly */
        color: #8892b0;
    }
    
    /* REMOVES SPACE BETWEEN PARAGRAPHS */
    .summary-text p {
        margin-bottom: 8px !important; /* Tightened the gap from default 20px+ to 8px */
    }

    h1, h2, h3 { color: #ccd6f6 !important; font-weight: 700; }
    
    /* Profile Photo Frame */
    [data-testid="stImage"] {
        border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); 
        max-width: 280px; 
        margin: auto;
        border: 2px solid #172a45;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EXECUTIVE SUMMARY ---
st.write("---")
st.header("📌 Executive Summary")

# Wrap the content in a div with the 'summary-text' class
st.write(f"""
<div class="summary-text">
<p>As a seasoned Product Team Lead and automation expert, I thrive at the intersection of visionary product strategy and technical execution. With over six years of hands-on experience, I specialize in bridging the gap between innovative ideas and scalable solutions—empowering teams to automate processes, optimize workflows, and deliver impactful results.</p>
<p>My expertise spans team management, capacity planning, and forecasting, complemented by a strong foundation in competitive intelligence, product management, data analytics, and data visualization.</p>
<p>I am passionate about transforming complex challenges into clean, efficient code, enabling businesses to scale seamlessly and automate repetitive tasks. Driven by strategic thinking and a collaborative leadership style, I excel at aligning cross-functional teams with business objectives, ensuring projects are delivered on time and exceed expectations. Whether guiding product vision or architecting automation solutions, I am dedicated to fostering growth, innovation, and measurable success.</p>
</div>
""", unsafe_allow_html=True)
