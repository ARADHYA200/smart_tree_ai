"""
Garden Page - Browse all trees with search and filters
"""
import streamlit as st
from utils.data_loader import load_trees_data, filter_trees, get_unique_values
from components.cards import render_tree_card
from utils.qr_generator import generate_qr_code, qr_to_bytes

def render_garden():
    """Render garden with all trees"""
    
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">🌳 Garden</h1>
    <p style="color: #94a3b8; font-size: 14px;">Explore hundreds of trees from our database</p>
    """, unsafe_allow_html=True)
    
    # Load data
    trees = load_trees_data()
    
    # Search Bar
    st.markdown("<br>", unsafe_allow_html=True)
    search_text = st.text_input(
        "🔍 Search trees...",
        placeholder="Enter tree name or scientific name",
        key="garden_search"
    )
    
    # Filters
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Filters")
    
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)
    
    with filter_col1:
        countries = ['All Countries'] + list(get_unique_values(trees, 'country'))
        selected_country = st.selectbox("🌍 Country", countries)
    
    with filter_col2:
        climates = ['All Climates'] + list(get_unique_values(trees, 'climate'))
        selected_climate = st.selectbox("🌡️ Climate", climates)
    
    with filter_col3:
        spaces = ['All Sizes'] + list(get_unique_values(trees, 'space'))
        selected_space = st.selectbox("📏 Space Required", spaces)
    
    with filter_col4:
        purposes = ['All Purposes'] + list(get_unique_values(trees, 'purpose'))
        selected_purpose = st.selectbox("🎯 Purpose", purposes)
    
    # Apply filters
    filtered_trees = filter_trees(
        trees,
        country=selected_country,
        climate=selected_climate,
        space=selected_space,
        purpose=selected_purpose,
        search_text=search_text
    )
    
    # Results info
    st.markdown(f"""
    <p style="color: #94a3b8; font-size: 13px; margin-top: 16px;">
    📊 Showing <b>{len(filtered_trees)}</b> trees
    </p>
    """, unsafe_allow_html=True)
    
    # Display trees in grid
    if filtered_trees:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Pagination
        trees_per_page = 12
        total_pages = (len(filtered_trees) + trees_per_page - 1) // trees_per_page
        
        page = st.selectbox("Page", range(1, total_pages + 1))
        
        start_idx = (page - 1) * trees_per_page
        end_idx = start_idx + trees_per_page
        page_trees = filtered_trees[start_idx:end_idx]
        
        # Create columns for grid layout
        cols = st.columns(3)
        
        for idx, tree in enumerate(page_trees):
            col = cols[idx % 3]
            
            with col:
                with st.container():
                    # Tree image
                    try:
                        st.image(tree['image'], use_column_width=True)
                    except:
                        st.markdown("""
                        <div style="background: rgba(6,182,212,0.1); height: 200px; 
                                   border-radius: 8px; display: flex; align-items: center; 
                                   justify-content: center; color: #94a3b8;">
                        Image unavailable
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Tree details
                    render_tree_card(tree)
                    
                    # Action buttons
                    btn_col1, btn_col2 = st.columns(2)
                    
                    with btn_col1:
                        if st.button("⭐ Add to Favorites", key=f"fav_{tree['id']}"):
                            if 'favorites' not in st.session_state:
                                st.session_state.favorites = []
                            if tree['id'] not in st.session_state.favorites:
                                st.session_state.favorites.append(tree['id'])
                                st.success("Added to favorites!")
                            else:
                                st.info("This tree is already in your favorites")
                    
                    with btn_col2:
                        if st.button("📱 QR Code", key=f"qr_{tree['id']}"):
                            qr_img = generate_qr_code(tree['name'], tree['id'])
                            st.image(qr_img, width=150)
                            
                            buf = qr_to_bytes(qr_img)
                            st.download_button(
                                label="⬇️ Download QR",
                                data=buf,
                                file_name=f"tree_{tree['id']}_qr.png",
                                mime="image/png"
                            )
    else:
        st.markdown("""
        <div style="text-align: center; padding: 40px; color: #94a3b8;">
        <p style="font-size: 16px;">🔍 No trees found matching your filters</p>
        <p style="font-size: 13px;">Try adjusting your search criteria</p>
        </div>
        """, unsafe_allow_html=True)
