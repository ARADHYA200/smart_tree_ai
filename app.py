"""
Smart Tree AI Pro - Main Application
Ultra-advanced production-level tree intelligence platform
"""
import streamlit as st
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from components.sidebar import render_sidebar
from components.cards import render_tree_card
from utils.data_loader import load_trees_data
from views.dashboard import render_dashboard
from views.garden import render_garden
from views.image_ai import render_image_ai
from views.recommendation import render_recommendations
from views.chatbot import render_chatbot
from views.tree_detail import render_tree_detail

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Smart Tree AI Pro",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com',
        'Report a bug': "https://github.com/issues",
        'About': "# Smart Tree AI Pro v1.0\n\nProduction-level tree intelligence platform"
    }
)

# ==========================================
# THEME & STYLING
# ==========================================

# Theme styling is applied dynamically after session state is initialized

# ==========================================
# INITIALIZE SESSION STATE
# ==========================================

if 'favorites' not in st.session_state:
    st.session_state.favorites = []

if 'recently_viewed' not in st.session_state:
    st.session_state.recently_viewed = []

dark_mode = st.session_state.get('dark_mode', True)
if 'dark_mode' not in st.session_state:
    try:
        st.session_state.dark_mode = dark_mode
    except Exception:
        pass

# ==========================================
# THEME & STYLING
# ==========================================

dark_colors = {
    'background_top': '#0f172a',
    'background_bottom': '#020617',
    'panel_bg': 'rgba(15,23,42,0.95)',
    'text': '#e2e8f0',
    'muted_text': '#cbd5e1',
    'accent': '#06b6d4',
    'card_bg': 'rgba(15,23,42,0.88)',
    'input_bg': 'rgba(255,255,255,0.06)',
    'border': 'rgba(6,182,212,0.18)'
}

light_colors = {
    'background_top': '#f8fafc',
    'background_bottom': '#e2e8f6',
    'panel_bg': 'rgba(255,255,255,0.96)',
    'text': '#0f172a',
    'muted_text': '#475569',
    'accent': '#2563eb',
    'card_bg': 'rgba(255,255,255,0.98)',
    'input_bg': 'rgba(15,23,42,0.05)',
    'border': 'rgba(37,99,235,0.18)'
}

colors = dark_colors if dark_mode else light_colors

st.markdown(f"""
<style>
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body, .css-18e3th9 {{
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.75;
    color: {colors['text']} !important;
}}

.stApp {{
    background: linear-gradient(135deg, {colors['background_top']} 0%, {colors['background_bottom']} 100%);
    color: {colors['text']} !important;
}}

section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {colors['background_top']} 0%, {colors['background_bottom']} 100%) !important;
    border-right: 1px solid {colors['border']} !important;
}}

.stMainBlockContainer {{
    padding-top: 0 !important;
}}

h1 {{
    font-size: 36px !important;
    font-weight: 700 !important;
    margin-bottom: 10px !important;
}}

h2 {{
    font-size: 28px !important;
    font-weight: 650 !important;
    margin-top: 22px !important;
}}

h3 {{
    font-size: 22px !important;
    font-weight: 600 !important;
    margin-top: 18px !important;
}}

p, label, span, .stText, .stMarkdown {{
    color: {colors['muted_text']} !important;
    font-size: 15px !important;
}}

.stButton > button {{
    background: linear-gradient(90deg, {colors['accent']}, #06b6d4) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 22px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}}

.stButton > button:hover {{
    box-shadow: 0 0 20px rgba(6,182,212,0.24) !important;
    transform: translateY(-1px) !important;
}}

input, select, textarea {{
    background: {colors['input_bg']} !important;
    border: 1px solid {colors['border']} !important;
    color: {colors['text']} !important;
    border-radius: 12px !important;
    padding: 12px 14px !important;
    font-size: 15px !important;
}}

input:focus, select:focus, textarea:focus {{
    border-color: {colors['accent']} !important;
    box-shadow: 0 0 0 3px rgba(6,182,212,0.12) !important;
}}

button[role="tab"] {{
    color: {colors['muted_text']} !important;
    font-size: 16px !important;
}}

button[role="tab"][aria-selected="true"] {{
    color: {colors['accent']} !important;
    border-bottom: 2px solid {colors['accent']} !important;
}}

.streamlit-expanderHeader {{
    background: rgba(6,182,212,0.1) !important;
    color: {colors['text']} !important;
    border-radius: 10px !important;
}}

.streamlit-expanderHeader:hover {{
    background: rgba(6,182,212,0.18) !important;
}}

::-webkit-scrollbar {{
    width: 10px;
    height: 10px;
}}

::-webkit-scrollbar-track {{
    background: rgba(255,255,255,0.08);
}}

::-webkit-scrollbar-thumb {{
    background: rgba(6,182,212,0.4);
    border-radius: 6px;
}}

::-webkit-scrollbar-thumb:hover {{
    background: rgba(6,182,212,0.6);
}}

@keyframes fadeIn {{
    from {{
        opacity: 0;
        transform: translateY(10px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.stApp {{
    animation: fadeIn 0.45s ease-in-out;
}}

</style>
""", unsafe_allow_html=True)

# ==========================================
# MAIN APPLICATION
# ==========================================

# Render sidebar and get page selection
selected_page = render_sidebar()
params = st.experimental_get_query_params()
tree_param = params.get("tree", [None])[0]
if tree_param is not None:
    selected_page = "tree_detail"

# Route to selected page
if selected_page == "🏠 Dashboard":
    render_dashboard()

elif selected_page == "🌳 Garden":
    render_garden()

elif selected_page == "🤖 Image AI":
    render_image_ai()

elif selected_page == "💡 Recommendations":
    render_recommendations()

elif selected_page == "💬 Chatbot":
    render_chatbot()

elif selected_page == "tree_detail":
    render_tree_detail()

elif selected_page == "⭐ Favorites":
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">⭐ Your Favorites</h1>
    <p style="color: #94a3b8; font-size: 14px;">Trees you've saved for later</p>
    """, unsafe_allow_html=True)
    
    favorite_ids = list(dict.fromkeys(st.session_state.get('favorites', [])))
    trees = load_trees_data()
    favorite_trees = [tree for tree in trees if tree['id'] in favorite_ids]

    if favorite_trees:
        st.success(f"You have {len(favorite_trees)} favorite tree(s) saved!")
        st.markdown("<br>", unsafe_allow_html=True)
        for tree in favorite_trees:
            render_tree_card(tree)
    else:
        st.info("💡 Start adding trees to your favorites! Click the star icon in the Garden or Recommendations section.")

elif selected_page == "⚙️ Settings":
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">⚙️ Settings</h1>
    <p style="color: #94a3b8; font-size: 14px;">Customize your experience</p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # General Settings
    with st.expander("🎨 Appearance", expanded=True):
        st.checkbox("Dark Mode", key="dark_mode")
        
        if st.session_state.dark_mode:
            st.success("🌙 Dark mode is enabled")
        else:
            st.info("☀️ Light mode is enabled")
    
    # Data Settings
    with st.expander("📊 Data", expanded=False):
        st.markdown("""
        - **Trees in Database**: Combined India + US datasets
        - **Total Records**: 600+ trees
        - **Last Updated**: 2024
        """)
        
        if st.button("🔄 Refresh Data Cache"):
            st.cache_resource.clear()
            st.success("Cache cleared! Data will be reloaded on next use.")
    
    # About
    with st.expander("ℹ️ About Smart Tree AI Pro", expanded=False):
        st.markdown("""
        ## Smart Tree AI Pro v1.0
        
        **An Ultra-Advanced Tree Intelligence Platform**
        
        ### Features
        - 🌳 Browse 600+ trees from India and US
        - 🤖 AI-powered image recognition
        - 💡 Smart recommendation engine
        - 🎯 Advanced filtering and search
        - 📊 Real-time analytics dashboard
        - 💬 AI chatbot for tree advice
        
        ### Technology Stack
        - Streamlit (Frontend)
        - Python (Backend)
        - Machine Learning (Image Classification)
        - Plotly (Data Visualization)
        
        ### Built with ❤️ for Tree Lovers
        """)

# ==========================================
# FOOTER
# ==========================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 20px; border-top: 1px solid rgba(6,182,212,0.1); margin-top: 40px;">
<p style="color: #94a3b8; font-size: 12px; margin: 0;">
🌿 Smart Tree AI Pro v1.0 | Built for Tree Enthusiasts & Environmentalists
</p>
<p style="color: #64748b; font-size: 11px; margin-top: 8px;">
Made with 🌱 • Powered by AI • For a Greener Tomorrow
</p>
</div>
""", unsafe_allow_html=True)
