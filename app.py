import streamlit as st

st.set_page_config(
    page_title="Satwik Parasar | AI/ML Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

GITHUB = "https://github.com/Albusxx-01"
LINKEDIN = "https://www.linkedin.com/in/satwik-parasar-a529b1214/"
EMAIL = "satwikxofficial@gmail.com"

# ----------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------
PROJECTS = {
    "Machine Learning": [
        {
            "name": "CinemaPulse — Movie Recommendation App",
            "repo": "CinemaPulse---Movie-Recommendation-Web-App",
            "desc": "Interactive movie recommendation web app built with Streamlit using NLP, CountVectorizer, and cosine similarity.",
            "tech": ["Python", "Streamlit", "NLP", "sklearn"],
            "url": "https://github.com/Albusxx-01/CinemaPulse---Movie-Recommendation-Web-App",
            "featured": True,
        },
        {
            "name": "Movie Recommendation System",
            "repo": "EDA-ML_Movie-Recommendation-System",
            "desc": "Content-based recommendation engine using NLP, Bag of Words, and cosine similarity to suggest similar movies.",
            "tech": ["Python", "NLP", "Pandas"],
            "url": "https://github.com/Albusxx-01/EDA-ML_Movie-Recommendation-System",
            "featured": False,
        },
        {
            "name": "Email/SMS Spam Classifier App",
            "repo": "ML_Email-SMS-Spam-Classifiers-App",
            "desc": "Spam detection app powered by a Multinomial Naive Bayes classifier.",
            "tech": ["Python", "Streamlit", "NLP"],
            "url": "https://github.com/Albusxx-01/ML_Email-SMS-Spam-Classifiers-App",
            "featured": False,
        },
        {
            "name": "Email/SMS Spam Classifier — NLP Pipeline",
            "repo": "DA-ML_Email-SMS-Spam-Classifier",
            "desc": "End-to-end NLP pipeline: EDA, preprocessing, vectorization, and multi-model classifier comparison.",
            "tech": ["Python", "NLP", "sklearn"],
            "url": "https://github.com/Albusxx-01/DA-ML_Email-SMS-Spam-Classifier",
            "featured": False,
        },
        {
            "name": "Car Price Predictor (EDA + Model)",
            "repo": "EDA_Car-Price-Predictor",
            "desc": "ML-based car price estimation using regression techniques with full EDA.",
            "tech": ["Python", "Pandas", "Regression"],
            "url": "https://github.com/Albusxx-01/EDA_Car-Price-Predictor",
            "featured": False,
        },
        {
            "name": "Car Price Predictor (UI)",
            "repo": "Car-Price-Perdictor",
            "desc": "Frontend interface for the car price prediction model.",
            "tech": ["HTML", "CSS", "JS"],
            "url": "https://github.com/Albusxx-01/Car-Price-Perdictor",
            "featured": False,
        },
        {
            "name": "Titanic Survival Predictor",
            "repo": "DA-Titanic_ML",
            "desc": "Classification model for Titanic survival with preprocessing, feature engineering, and Logistic Regression.",
            "tech": ["Python", "Classification", "EDA"],
            "url": "https://github.com/Albusxx-01/DA-Titanic_ML",
            "featured": False,
        },
    ],
    "Data Analytics": [
        {
            "name": "IPL Data Analysis (2008–2024)",
            "repo": "DA_IPL",
            "desc": "In-depth EDA of the IPL using Python, Pandas, and Seaborn — team performance, player stats, and match outcomes.",
            "tech": ["Python", "Pandas", "Seaborn"],
            "url": "https://github.com/Albusxx-01/DA_IPL",
            "featured": True,
        },
        {
            "name": "Spotify 2024 Analysis",
            "repo": "DA-Spotify",
            "desc": "Analysis of the most-streamed Spotify songs of 2024 — outlier removal and cross-platform streaming trends.",
            "tech": ["Python", "Pandas", "Seaborn"],
            "url": "https://github.com/Albusxx-01/DA-Spotify",
            "featured": False,
        },
        {
            "name": "Netflix Data Analysis",
            "repo": "DA_Netflix",
            "desc": "Insights on content distribution, genres, countries, directors, and ratings — ML-ready dataset prep.",
            "tech": ["Python", "Pandas"],
            "url": "https://github.com/Albusxx-01/DA_Netflix",
            "featured": False,
        },
        {
            "name": "Adult Income (Census) EDA",
            "repo": "DA-Income_slip",
            "desc": "EDA on the Adult Income dataset — cleaning, transformation, and demographic insights.",
            "tech": ["Python", "Pandas"],
            "url": "https://github.com/Albusxx-01/DA-Income_slip",
            "featured": False,
        },
        {
            "name": "E-commerce Purchase Analysis",
            "repo": "DA-Ecommerce",
            "desc": "EDA on e-commerce customer purchase data to uncover behavioral and transactional insights.",
            "tech": ["Python", "Pandas"],
            "url": "https://github.com/Albusxx-01/DA-Ecommerce",
            "featured": False,
        },
    ],
    "Web Development": [
        {
            "name": "iReader — Bootstrap Website",
            "repo": "iReader-Bootstrap",
            "desc": "Book-reading themed responsive website built with Bootstrap.",
            "tech": ["HTML", "CSS", "Bootstrap"],
            "url": "https://github.com/Albusxx-01/iReader-Bootstrap",
            "featured": False,
        },
    ],
}

SKILLS = [
    ("Python", "🐍"),
    ("Go", "🐹"),
    ("Java", "☕"),
    ("FastAPI", "⚡"),
    ("Flask", "🍶"),
    ("Streamlit", "📊"),
    ("TensorFlow", "🧠"),
    ("PyTorch", "🔥"),
    ("Docker", "🐳"),
    ("MongoDB", "🍃"),
    ("PostgreSQL", "🐘"),
    ("Jupyter", "📓"),
    ("Linux", "🐧"),
    ("Git", "🌿"),
]

STATS = [
    ("14", "Repositories"),
    ("13", "Projects"),
    ("3", "Core Domains"),
    ("10+", "Data & ML Projects"),
]

# ----------------------------------------------------------------------------
# Global CSS
# ----------------------------------------------------------------------------
def inject_css():
    st.markdown(
        """
        <style>
        :root {
            --bg: #0b0e14;
            --bg-soft: #121722;
            --card: #151b28;
            --border: #232b3b;
            --text: #e6e9f0;
            --muted: #9aa4b8;
            --primary: #7c3aed;
            --accent: #6366f1;
            --cyan: #22d3ee;
            --green: #34d399;
        }

        .stApp {
            background:
                radial-gradient(1200px 600px at 85% -10%, rgba(124,58,237,0.18), transparent 60%),
                radial-gradient(900px 500px at -10% 20%, rgba(34,211,238,0.10), transparent 55%),
                var(--bg);
            color: var(--text);
            font-family: 'Segoe UI', -apple-system, sans-serif;
        }

        h1, h2, h3, h4 { letter-spacing: -0.02em; }

        /* Hero */
        .hero { padding: 2.2rem 0 1rem; }
        .hero-name {
            font-size: 3.4rem;
            font-weight: 800;
            background: linear-gradient(120deg, #fff 0%, #c7b8ff 45%, var(--primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            line-height: 1.05;
        }
        .hero-title {
            font-size: 1.35rem;
            font-weight: 600;
            color: var(--cyan);
            margin: 0.6rem 0 0.2rem;
            letter-spacing: 0.02em;
        }
        .hero-tag {
            color: var(--muted);
            font-size: 1.02rem;
            margin: 0.4rem 0 1.2rem;
        }
        .badge {
            display: inline-block;
            background: rgba(124,58,237,0.14);
            border: 1px solid rgba(124,58,237,0.4);
            color: #d8cbfd;
            padding: 0.28rem 0.8rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 500;
            margin: 0.15rem 0.2rem 0.15rem 0;
            letter-spacing: 0.01em;
        }
        .avatar {
            border-radius: 50%;
            border: 3px solid var(--primary);
            box-shadow: 0 0 30px rgba(124,58,237,0.45);
            width: 100%;
            max-width: 250px;
            display: block;
            margin: 0 auto;
        }
        .social-btn {
            display: inline-flex; align-items: center; gap: 0.5rem;
            text-decoration: none;
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 0.55rem 1.3rem;
            border-radius: 12px;
            font-weight: 600;
            font-size: 0.92rem;
            transition: all .2s ease;
        }
        .social-btn:hover {
            transform: translateY(-2px);
            border-color: var(--primary);
            box-shadow: 0 8px 24px rgba(124,58,237,0.35);
            color: #fff;
        }
        .social-btn.github { background: linear-gradient(135deg,#191d27,#242b3b); }
        .social-btn.linkedin { background: linear-gradient(135deg,#0a66c2,#0a4d8f); border-color:#0a66c2; }
        .social-btn.mail { background: linear-gradient(135deg,#d14836,#a8311f); border-color:#d14836; }

        .section-title {
            font-size: 1.6rem; font-weight: 700; margin: 2rem 0 0.4rem;
            display: flex; align-items: center; gap: 0.6rem;
        }
        .section-title span.sep { color: var(--primary); }

        /* Stats */
        .stat-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.1rem;
            text-align: center;
            box-shadow: 0 4px 18px rgba(0,0,0,0.35);
        }
        .stat-num {
            font-size: 1.9rem; font-weight: 800;
            background: linear-gradient(120deg, var(--primary), var(--cyan));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .stat-label { color: var(--muted); font-size: 0.85rem; margin-top: 0.2rem; }

        /* Skill chips */
        .chip {
            display: inline-flex; align-items: center; gap: 0.45rem;
            background: var(--card);
            border: 1px solid var(--border);
            padding: 0.5rem 1rem;
            border-radius: 10px;
            font-weight: 600; font-size: 0.92rem;
            margin: 0.25rem;
            transition: all .18s ease;
        }
        .chip:hover {
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(124,58,237,0.3);
        }

        /* Project card (hypercard style HTML) */
        .proj {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.15rem 1.25rem;
            margin-bottom: 1rem;
            transition: all .2s ease;
            height: 100%;
            display: flex; flex-direction: column;
        }
        .proj:hover {
            border-color: rgba(124,58,237,0.6);
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(124,58,237,0.22);
        }
        .proj-name { font-size: 1.05rem; font-weight: 700; color: #fff; margin-bottom: 0.3rem; }
        .proj-desc { color: var(--muted); font-size: 0.88rem; line-height: 1.5; flex: 1; }
        .proj-tech { margin-top: 0.7rem; }
        .proj-star { color: #fbbf24; font-size: 0.8rem; font-weight: 700; }
        .link-btn {
            display: inline-block; margin-top: 0.9rem;
            color: var(--cyan); font-weight: 600; font-size: 0.85rem;
            text-decoration: none;
        }
        .link-btn:hover { text-decoration: underline; }

        .featured {
            border: 1px solid rgba(124,58,237,0.55);
            background: linear-gradient(160deg, rgba(124,58,237,0.10), var(--card) 45%);
        }

        /* Pill filter */
        .stButton > button {
            border-radius: 999px;
            border: 1px solid var(--border);
            background: var(--card);
            color: var(--text);
            font-weight: 600;
            padding: 0.4rem 1.2rem;
            transition: all .2s ease;
        }
        .stButton > button:hover {
            border-color: var(--primary);
            box-shadow: 0 4px 16px rgba(124,58,237,0.4);
        }

        /* ------------------------- Sidebar ------------------------- */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0c0f17 0%, #111624 100%);
            border-right: 1px solid var(--border);
            padding-top: 0.6rem;
        }
        [data-testid="stSidebar"]::before {
            content: "";
            display: block;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--cyan), var(--primary));
            background-size: 200% 100%;
            animation: barflow 6s linear infinite;
            margin: -1.2rem -1rem 0.5rem;
        }
        @keyframes barflow { to { background-position: 200% 0; } }

        /* profile card */
        .sb-av-wrap {
            position: relative; width: 108px; height: 108px; margin: 0 auto 0.7rem;
            border-radius: 50%;
            background: conic-gradient(from 210deg, #7c3aed, #6366f1, #22d3ee, #7c3aed);
            padding: 3px;
        }
        .sb-av {
            border-radius: 50%; width: 100%; height: 100%;
            object-fit: cover; display: block;
            border: 3px solid #0c0f17;
        }
        .sb-name {
            font-size: 1.18rem; font-weight: 800; text-align: center; color: #fff;
            background: linear-gradient(120deg, #fff, #c7b8ff, var(--color, #7c3aed));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .sb-role { text-align: center; color: var(--cyan); font-size: 0.82rem; font-weight: 600; }
        .sb-status {
            display: flex; align-items: center; justify-content: center; gap: 0.45rem;
            margin: 0.6rem auto 0; width: fit-content;
            color: #a7e8c8; font-size: 0.75rem; font-weight: 600;
            background: rgba(52,211,153,0.10); border: 1px solid rgba(52,211,153,0.4);
            border-radius: 999px; padding: 0.22rem 0.75rem;
        }
        .sb-dot {
            width: 8px; height: 8px; border-radius: 50%; background: #34d399;
            animation: pulse 1.6s ease-in-out infinite;
        }
        @keyframes pulse {
            0%,100% { box-shadow: 0 0 0 0 rgba(52,211,153,0.5); }
            50%      { box-shadow: 0 0 0 6px rgba(52,211,153,0); }
        }

        .sb-head {
            font-size: 0.68rem; letter-spacing: 0.14em; color: var(--muted);
            font-weight: 700; margin: 1.1rem 0 0.35rem; padding-left: 2px;
        }

        /* push contact block to the bottom of the panel */
        [data-testid="stSidebarUserContent"] { display: flex; flex-direction: column; }
        [data-testid="stSidebarUserContent"] .block-container {
            display: flex; flex-direction: column; flex: 1;
        }
        .sb-contact { margin-top: auto; padding-top: 1.2rem; }

        /* nav pills — restyle the radio */
        [data-testid="stSidebar"] [role="radiogroup"] {
            display: flex; flex-direction: column; gap: 0.4rem;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 0.55rem 0.9rem;
            min-height: 42px;
            color: var(--muted);
            font-weight: 600;
            transition: all .18s ease;
            display: flex; align-items: center;
            cursor: pointer;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label:hover {
            border-color: rgba(124,58,237,0.6);
            color: #fff;
            transform: translateX(3px);
        }
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
            background: linear-gradient(120deg, rgba(124,58,237,0.28), rgba(99,102,241,0.18));
            border-color: var(--primary);
            color: #fff;
            box-shadow: 0 4px 18px rgba(124,58,237,0.35);
        }

        /* mini contact lines */
        .sb-line { font-size: 0.82rem; color: var(--muted); display: flex; gap: 0.5rem; align-items: center; }
        .sb-line a { color: var(--muted); text-decoration: none; }
        .sb-line a:hover { color: var(--cyan); }

        /* socials row */
        .sb-socials { display: flex; justify-content: center; gap: 0.5rem; }
        .sb-social {
            width: 36px; height: 36px; border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            background: var(--card); border: 1px solid var(--border);
            color: var(--muted); font-size: 1rem; text-decoration: none;
            transition: all .18s ease;
        }
        .sb-social:hover {
            border-color: var(--primary); color: #fff;
            transform: translateY(-3px);
            box-shadow: 0 6px 18px rgba(124,58,237,0.4);
        }

        .sb-foot { text-align: center; color: var(--muted); font-size: 0.72rem; margin-top: 0.2rem; }

        /* Footer */
        .footer {
            text-align: center; color: var(--muted);
            font-size: 0.85rem; padding: 2rem 0 0.5rem;
            border-top: 1px solid var(--border); margin-top: 2rem;
        }

        /* timestamps / info line */
        .info-line { color: var(--muted); font-size: 0.9rem; }

        /* hide streamlit chrome */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stToolbar"] {display: none;}

        /* custom selectbox for filter */
        div[data-testid="stSelectbox"] label { color: var(--muted); font-size: 0.85rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )


AVATAR_URL = "https://avatars.githubusercontent.com/u/150047431?v=4"

# ----------------------------------------------------------------------------
# Sections
# ----------------------------------------------------------------------------
def render_hero():
    c1, c2 = st.columns([2.1, 1], gap="large")
    with c1:
        st.markdown(
            """
            <div class="hero">
                <p class="hero-title">Hi, I'm</p>
                <h1 class="hero-name">Satwik Parasar</h1>
                <p class="hero-title">✦ AI/ML Engineer & Backend Developer</p>
                <p class="hero-tag">
                    B.Tech Computer Science student building intelligent systems — from multimodal RAG pipelines
                    to code-mixed AI solutions. Currently exploring <b>Edge AI</b>, <b>Small Language Models</b> & <b>Code-Mixed ASR</b>.
                </p>
                <div>
                    <a class="social-btn github" href="https://github.com/Albusxx-01" target="_blank">★ GitHub</a>
                    <a class="social-btn linkedin" href="https://www.linkedin.com/in/satwik-parasar-a529b1214/" target="_blank">in LinkedIn</a>
                    <a class="social-btn mail" href="mailto:satwikxofficial@gmail.com">✉ Email</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<img class="avatar" src="{AVATAR_URL}" alt="profile"/>',
            unsafe_allow_html=True,
        )


def render_stats():
    cols = st.columns(4)
    for col, (num, label) in zip(cols, STATS):
        with col:
            st.markdown(
                f'<div class="stat-card"><div class="stat-num">{num}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True,
            )


def render_about():
    st.markdown(
        """
        <div class="section-title"><span class="sep">▍</span> About Me</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        I'm an AI/ML engineer passionate about data, machine learning, and backend systems.
        I love turning raw data into real products — from movie recommendation engines and spam
        classifiers to large-scale EDA. I write clean, efficient, and scalable code and I'm always
        building something new.

        **What I'm focusing on right now:** Edge AI, Small Language Models, and Code-Mixed ASR.
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "**Core strengths:** " + " ".join(
            f'<span class="badge">{t}</span>' for t in
            ["Artificial Intelligence", "Machine Learning", "Data Analysis",
             "Multimodal RAG", "Backend Engineering", "Problem Solving"]
        ),
        unsafe_allow_html=True,
    )


def render_skills():
    st.markdown(
        '<div class="section-title"><span class="sep">▍</span> Tech Stack</div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    half = (len(SKILLS) + 1) // 2
    for idx, (name, icon) in enumerate(SKILLS):
        col = cols[0] if idx < half else cols[1]
        with col:
            st.markdown(f'<div class="chip">{icon} {name}</div>', unsafe_allow_html=True)


def card_for(proj):
    tech = " ".join(f'<span class="badge">{t}</span>' for t in proj["tech"])
    top = ""
    if proj.get("featured"):
        top = '<div class="proj-star">★ FEATURED</div>'
    return (
        '<div class="proj {featured}">'
        f'<div class="proj-name">{proj["name"]}</div>'
        f'<div class="proj-desc">{proj["desc"]}</div>'
        f'<div class="proj-tech">{tech}</div>'
        f'{top}'
        f'<a class="link-btn" href="{proj["url"]}" target="_blank">View on GitHub →</a>'
        "</div>"
    ).format(featured="featured" if proj.get("featured") else "")


def render_projects():
    st.markdown(
        '<div class="section-title"><span class="sep">▍</span> Projects</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="info-line">Filter by category — top cards are featured highlights.</p>',
        unsafe_allow_html=True,
    )
    cats = list(PROJECTS.keys()) + ["All"]
    selected = st.selectbox("Filter:", cats, label_visibility="collapsed")
    items = []
    if selected == "All":
        items = [p for group in PROJECTS.values() for p in group]
    else:
        items = PROJECTS[selected]
    items = sorted(items, key=lambda x: not x.get("featured"))

    per_row = 2 if selected != "All" or len(items) > 4 else min(2, len(items))
    for i in range(0, len(items), per_row):
        row = items[i : i + per_row]
        cols = st.columns(per_row)
        for col, proj in zip(cols, row):
            with col:
                st.markdown(card_for(proj), unsafe_allow_html=True)


def render_github():
    st.markdown(
        '<div class="section-title"><span class="sep">▍</span> GitHub Activity</div>',
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f'<img src="https://github-readme-stats.vercel.app/api?username=Albusxx-01&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&bg_color=0b0e14" style="border-radius:14px;width:100%"/>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Albusxx-01&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b0e14" style="border-radius:14px;width:100%"/>',
            unsafe_allow_html=True,
        )


def render_contact():
    st.markdown(
        '<div class="section-title"><span class="sep">▍</span> Get In Touch</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        Always happy to chat about AI, ML, data, or potential collaborations.
        Feel free to reach out on any platform — I try to reply quickly.
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<a class="social-btn github" style="width:100%;justify-content:center" href="https://github.com/Albusxx-01" target="_blank">★ GitHub</a>', unsafe_allow_html=True)
    with c2:
        st.markdown('<a class="social-btn linkedin" style="width:100%;justify-content:center" href="https://www.linkedin.com/in/satwik-parasar-a529b1214/" target="_blank">in LinkedIn</a>', unsafe_allow_html=True)
    with c3:
        st.markdown('<a class="social-btn mail" style="width:100%;justify-content:center" href="mailto:satwikxofficial@gmail.com">✉ Email Me</a>', unsafe_allow_html=True)


def footer():
    st.markdown(
        '<div class="footer">Designed & built with ⚡ Streamlit · © 2026 Satwik Parasar</div>',
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------------------------
# Sidebar / navigation
# ----------------------------------------------------------------------------
def sidebar():
    with st.sidebar:
        st.markdown(
            '<div style="text-align:center;padding:.4rem 0 .2rem">'
            '<div class="sb-av-wrap">'
            f'<img class="sb-av" src="{AVATAR_URL}"/>'
            "</div>"
            '<div class="sb-name">Satwik Parasar</div>'
            '<div class="sb-role">◆ AI/ML Engineer &nbsp;·&nbsp; Backend Dev</div>'
            '<div class="sb-status"><span class="sb-dot"></span>Open to opportunities</div>'
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown('<div class="sb-head">MENU</div>', unsafe_allow_html=True)
        section = st.radio(
            "Navigate",
            ["✨ Home", "🚀 Projects", "📬 Contact"],
            label_visibility="collapsed",
        )
        section = section.split(" ", 1)[-1]
        st.markdown(
            '<div class="sb-contact">'
            '<div class="sb-head">CONTACT</div>'
            '<div style="height:1px;background:var(--border);margin:.6rem 0 .9rem"></div>'
            f'<div class="sb-line">✉ <a href="mailto:{EMAIL}">{EMAIL}</a></div>'
            f'<div class="sb-line">★ <a href="{GITHUB}" target="_blank">github.com/Albusxx-01</a></div>'
            '<div class="sb-line" style="margin-top:.7rem">Open to collaborations</div>'
            '<div class="sb-socials" style="margin-top:.8rem">'
            f'<a class="sb-social" title="GitHub" href="{GITHUB}" target="_blank">★</a>'
            f'<a class="sb-social" title="LinkedIn" href="{LINKEDIN}" target="_blank">in</a>'
            f'<a class="sb-social" title="Email" href="mailto:{EMAIL}">✉</a>'
            "</div>"
            '<div class="sb-foot" style="margin-top:1rem">© 2026 · Built with Streamlit ⚡</div>'
            "</div>",
            unsafe_allow_html=True,
        )
        return section


def main():
    inject_css()
    section = sidebar()
    if section == "Home":
        render_hero()
        st.markdown("<br/>", unsafe_allow_html=True)
        render_stats()
        st.markdown("---")
        render_about()
        st.markdown("---")
        render_skills()
        st.markdown("---")
        render_projects()
    elif section == "Projects":
        render_github()
        st.markdown("---")
        render_projects()
    elif section == "Contact":
        render_contact()
        st.markdown("---")
        render_about()
    footer()


main()