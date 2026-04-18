"""
Sidebar Navigation Component
"""
import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar() -> str:
    """
    Render sidebar with navigation
    Returns selected page
    """
    with st.sidebar:
        st.markdown("""
        <style>
        .sidebar-title {
            font-size: 32px;
            font-weight: 800;
            background: linear-gradient(90deg, #06b6d4, #2563eb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 24px;
        }
        </style>
        <div class="sidebar-title">🌿 Smart Tree AI</div>
        """, unsafe_allow_html=True)
        
        # Sidebar navigation menu
        selected = option_menu(
            menu_title=None,
            options=[
                "🏠 Dashboard",
                "🌳 Garden",
                "🤖 Image AI",
                "💡 Recommendations",
                "💬 Chatbot",
                "⭐ Favorites",
                "⚙️ Settings"
            ],
            icons=[
                "speedometer2",
                "tree-fill",
                "cpu",
                "lightbulb",
                "chat-dots",
                "star-fill",
                "gear"
            ],
            menu_icon="menu-app",
            default_index=0,
            styles={
                "container": {"padding": "0!important"},
                "icon": {"color": "#06b6d4", "font-size": "20px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "rgba(6,182,212,0.12)",
                    "padding": "14px 18px",
                    "border-radius": "10px",
                },
                "nav-link-selected": {"background-color": "rgba(37,99,235,0.28)"},
            }
        )
        
        st.markdown("---")
        
        # Sidebar footer
        st.markdown("""
        <style>
        .sidebar-footer {
            font-size: 12px;
            color: #94a3b8;
            text-align: center;
            margin-top: 40px;
        }
        </style>
        <div class="sidebar-footer">
            <p>🌍 Smart Tree AI Pro</p>
            <p>v1.0.0 | Production Ready</p>
        </div>
        """, unsafe_allow_html=True)
        
        return selected
