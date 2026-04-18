"""
Recommendations Page - Smart tree recommendation engine
"""
import streamlit as st
from utils.data_loader import load_trees_data, get_recommendations, get_unique_values
from components.cards import render_recommendation_card, render_tree_card

def render_recommendations():
    """Render recommendation engine page"""
    
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">💡 Smart Recommendations</h1>
    <p style="color: #94a3b8; font-size: 14px;">Get personalized tree suggestions based on your needs</p>
    """, unsafe_allow_html=True)
    
    # Load data
    trees = load_trees_data()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Input section
    st.markdown("##### Your Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Purpose
        purposes = list(set([p for tree in trees for p in tree['purpose']]))
        selected_purpose = st.selectbox(
            "🎯 What's your primary purpose?",
            purposes,
            help="Why do you want to plant a tree?"
        )
        
        # Space
        spaces = list(set([tree['space'] for tree in trees]))
        selected_space = st.selectbox(
            "📏 How much space do you have?",
            spaces,
            help="Available space for planting"
        )
    
    with col2:
        # Climate
        climates = list(set([tree['climate'] for tree in trees]))
        selected_climate = st.selectbox(
            "🌡️ What's your climate?",
            climates,
            help="Your local climate zone"
        )
        
        # Country
        countries = list(set([tree['country'] for tree in trees]))
        selected_country = st.selectbox(
            "🌍 Your country?",
            countries,
            help="Your location preference"
        )
    
    # Get recommendations
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Get Recommendations", type="primary"):
        recommendations = get_recommendations(
            trees,
            purpose=selected_purpose,
            space=selected_space,
            climate=selected_climate,
            country=selected_country
        )
        
        if recommendations:
            st.markdown("##### Top Recommendations for You")
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Display recommendations
            for idx, rec in enumerate(recommendations, 1):
                with st.container():
                    st.markdown(f"### #{idx} - {rec['name']} ({rec['match_score']:.1f}% match)")
                    
                    rec_col1, rec_col2, rec_col3 = st.columns([2, 1, 1])
                    
                    with rec_col1:
                        st.markdown(f"""
                        <div style="background: rgba(6,182,212,0.05); padding: 15px; border-radius: 8px;">
                        <p style="color: #94a3b8; font-style: italic; margin: 0 0 12px 0;">
                        {rec['scientific_name']}
                        </p>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Climate</p>
                        <p style="color: #e2e8f0; margin: 4px 0 12px 0;"><b>{rec['climate'].title()}</b></p>
                        </div>
                        <div>
                        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Space</p>
                        <p style="color: #e2e8f0; margin: 4px 0 12px 0;"><b>{rec['space'].title()}</b></p>
                        </div>
                        <div>
                        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Growth Rate</p>
                        <p style="color: #e2e8f0; margin: 4px 0 12px 0;"><b>{rec['growth_rate'].title()}</b></p>
                        </div>
                        <div>
                        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Oxygen</p>
                        <p style="color: #e2e8f0; margin: 4px 0 12px 0;"><b>{rec['oxygen']}/10</b></p>
                        </div>
                        </div>
                        
                        <p style="color: #cbd5e1; line-height: 1.6; margin-top: 12px;">
                        {rec['uses']}
                        </p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with rec_col2:
                        # Match score visualization
                        match_pct = rec['match_score']
                        match_color = "#06b6d4" if match_pct >= 70 else "#f59e0b" if match_pct >= 50 else "#ef4444"
                        
                        st.markdown(f"""
                        <div style="text-align: center; background: rgba(255,255,255,0.05); 
                                   padding: 15px; border-radius: 8px; border-left: 4px solid {match_color};">
                        <p style="color: #94a3b8; font-size: 12px; margin: 0 0 8px 0;">Match Score</p>
                        <p style="color: {match_color}; font-size: 28px; font-weight: bold; margin: 0;">
                        {match_pct:.0f}%
                        </p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with rec_col3:
                        if st.button("📖 Details", key=f"rec_details_{rec['id']}"):
                            st.session_state[f'show_details_{rec["id"]}'] = True
                        
                        if st.button("⭐ Favorite", key=f"rec_fav_{rec['id']}"):
                            if 'favorites' not in st.session_state:
                                st.session_state.favorites = []
                            if rec['id'] not in st.session_state.favorites:
                                st.session_state.favorites.append(rec['id'])
                                st.success("Added!")
                            else:
                                st.info("Already in favorites")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.warning("No recommendations found. Try different criteria.")
    
    # Tips section
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.expander("💡 Recommendation Tips", expanded=False):
        st.markdown("""
        - **Purpose**: Choose based on your main goal (oxygen, food, medicine, decoration)
        - **Space**: Smaller trees for apartments, larger for yards
        - **Climate**: Match your local weather patterns
        - **Location**: Local trees often thrive better in their native regions
        - **Higher match scores** indicate better suitability for your conditions
        """)
