

import streamlit as st
import pickle

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


# Even more attractive UI: animated background, glassmorphism, floating icon
st.markdown(
    """
    <style>
    body, .stApp {
        min-height: 100vh;
        background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        background-size: 200% 200%;
        animation: gradientMove 8s ease-in-out infinite alternate;
        font-family: 'Segoe UI', 'Roboto', sans-serif;
    }
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    .main-card {
        background: rgba(255,255,255,0.75);
        border-radius: 28px;
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.18), 0 1.5px 16px 0 rgba(99,102,241,0.08);
        padding: 3.2rem 2.5rem 2.5rem 2.5rem;
        max-width: 540px;
        margin: 3.5rem auto 2rem auto;
        border: 1.5px solid #e0e7ef;
        position: relative;
        animation: fadeInCard 1.2s cubic-bezier(.4,0,.2,1);
        backdrop-filter: blur(8px) saturate(1.2);
    }
    @keyframes fadeInCard {
        0% { opacity: 0; transform: translateY(40px) scale(0.98); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    .main-title {
        font-size: 2.6rem;
        font-weight: 900;
        color: #0e3eda;
        margin-bottom: 1.2rem;
        text-align: center;
        letter-spacing: 1px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.7rem;
        position: relative;
    }
    .logo-anim {
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 0.2rem;
        animation: floatLogo 2.2s infinite alternate cubic-bezier(.6,-0.28,.74,0.05);
        filter: drop-shadow(0 4px 16px #2563eb44);
        z-index: 2;
    }
    @keyframes floatLogo {
        0% { transform: translateY(0) scale(1) rotate(-8deg); }
        60% { transform: translateY(-12px) scale(1.08) rotate(8deg); }
        100% { transform: translateY(-8px) scale(1.04) rotate(-6deg); }
    }
    .email-label {
        font-size: 1.18rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.7rem;
        letter-spacing: 0.2px;
    }
    .stTextArea textarea {
        border-radius: 14px !important;
        border: 2px solid #a5b4fc !important;
        font-size: 1.08rem;
        min-height: 140px;
        background: #f8fafc !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: border 0.2s;
    }
    .stTextArea textarea:focus {
        border: 2px solid #6366f1 !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #6366f1 0%, #2563eb 100%);
        color: #fff;
        font-weight: 800;
        border-radius: 12px;
        padding: 0.9rem 2.7rem;
        font-size: 1.18rem;
        margin-top: 1.3rem;
        box-shadow: 0 2px 12px rgba(99,102,241,0.13);
        border: none;
        transition: background 0.2s, transform 0.1s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #2563eb 0%, #6366f1 100%);
        transform: translateY(-2px) scale(1.04);
    }
    .stAlert {
        border-radius: 12px !important;
        font-size: 1.13rem !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 16px rgba(255,0,0,0.07);
    }
    .stAlert[data-baseweb="alert"] .css-1w0ym84 {
        font-size: 1.22rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Main card with animated logo and title
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('''<div class="main-title"><span class="logo-anim"> 
        <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="48" height="48" rx="12" fill="#2563eb"/>
            <rect x="7" y="13" width="34" height="22" rx="4" fill="#fff"/>
            <rect x="7" y="13" width="34" height="22" rx="4" stroke="#a5b4fc" stroke-width="2"/>
            <ellipse cx="24" cy="24" rx="8" ry="6" fill="#a5b4fc"/>
            <ellipse cx="24" cy="24" rx="4" ry="3" fill="#2563eb"/>
            <text x="24" y="27" text-anchor="middle" font-size="10" font-family="Segoe UI, Arial" fill="#fff">@</text>
        </svg>
        </span>Spam Email Detection</div>''', unsafe_allow_html=True)

st.markdown('<div class="email-label">Enter email text</div>', unsafe_allow_html=True)
text = st.text_area("", key="email_text")

if st.button("Check", key="check_btn"):
    vector = vectorizer.transform([text])
    result = model.predict(vector)
    if result[0] == "spam":
        st.error("🚨 Spam Email")
    else:
        st.success("✅ Not Spam")

st.markdown('</div>', unsafe_allow_html=True)
