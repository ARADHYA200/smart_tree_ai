"""
Image AI Page - Upload image to detect tree species
"""
import streamlit as st
from PIL import Image
import io
from model.image_classifier import TreeImageClassifier, SimpleTreeMatcher
from utils.data_loader import load_trees_data
from utils.qr_generator import generate_qr_code, qr_to_bytes
from components.cards import render_tree_card

def render_image_ai():
    """Render image AI detection page"""
    
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">🤖 Image AI - Tree Detection</h1>
    <p style="color: #94a3b8; font-size: 14px;">Upload a tree photo and let AI identify it</p>
    """, unsafe_allow_html=True)
    
    # Load data
    trees = load_trees_data()
    
    # Upload area
    st.markdown("<br>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📸 Upload a tree image",
        type=['jpg', 'jpeg', 'png', 'webp'],
        help="Upload a clear photo of a tree for best results"
    )
    
    if uploaded_file:
        # Display uploaded image
        try:
            image = Image.open(uploaded_file).convert("RGB")
        except:
            st.error("Invalid image file")
            return
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("##### Original Image")
            st.image(image, use_column_width=True)
        
        with col2:
            st.markdown("##### Analysis")
            
            # Show loading spinner
            with st.spinner("🔍 Analyzing image..."):
                # Use tree classifier
                @st.cache_resource
                def get_classifier():
                    return TreeImageClassifier()

                classifier = get_classifier()
                
                # Get predictions
                predictions = classifier.predict_tree(image, trees, top_k=5)
                
                if predictions and len(predictions) > 0:
                    st.success("✅ Analysis complete!")
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Display predictions
                    st.markdown("##### Top Matches")
                    
                    for idx, (tree, confidence) in enumerate(predictions, 1):
                        with st.expander(
                            f"#{idx} {tree['name']} - {confidence:.1f}% confidence",
                            expanded=(idx == 1)
                        ):
                            pred_col1, pred_col2 = st.columns([2, 1])
                            
                            with pred_col1:
                                st.markdown(f"""
                                <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 8px;">
                                <h4 style="color: #06b6d4; margin-top: 0;">{tree['name']}</h4>
                                <p style="color: #94a3b8; font-style: italic; margin: 8px 0;">
                                {tree['scientific_name']}
                                </p>
                                
                                <div style="margin-top: 12px;">
                                <p style="color: #e2e8f0; margin: 8px 0;"><b>🌍 Region:</b> {tree['region']}</p>
                                <p style="color: #e2e8f0; margin: 8px 0;"><b>🌡️ Climate:</b> {tree['climate'].title()}</p>
                                <p style="color: #e2e8f0; margin: 8px 0;"><b>📏 Space:</b> {tree['space'].title()}</p>
                                <p style="color: #e2e8f0; margin: 8px 0;"><b>⏱️ Growth:</b> {tree['growth_rate'].title()}</p>
                                <p style="color: #e2e8f0; margin: 8px 0;"><b>📝 Uses:</b> {tree['uses']}</p>
                                </div>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Oxygen production bar
                                oxygen_pct = (tree['oxygen'] / 10) * 100
                                st.markdown(f"""
                                <div style="margin-top: 12px;">
                                <p style="color: #e2e8f0; font-size: 13px;">Oxygen Production</p>
                                <div style="background: rgba(255,255,255,0.1); height: 8px; border-radius: 4px; overflow: hidden;">
                                <div style="height: 100%; width: {oxygen_pct}%; background: linear-gradient(90deg, #06b6d4, #2563eb);"></div>
                                </div>
                                <p style="color: #94a3b8; font-size: 12px; margin-top: 4px;">{tree['oxygen']}/10</p>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            with pred_col2:
                                # QR Code
                                try:
                                    qr_img = generate_qr_code(tree['name'], tree['id'])
                                    st.image(qr_img, width=150)
                                    
                                    buf = qr_to_bytes(qr_img)
                                    st.download_button(
                                        label="⬇️ Download QR",
                                        data=buf,
                                        file_name=f"tree_{tree['id']}_qr.png",
                                        mime="image/png",
                                        key=f"dl_qr_{tree['id']}"
                                    )
                                except:
                                    st.info("QR generation unavailable")
                else:
                    st.warning("⚠️ Could not analyze image. Please try another image.")
    
    # Information section
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-left: 4px solid #06b6d4; 
                padding: 15px; border-radius: 8px; margin-top: 20px;">
    <h4 style="color: #06b6d4; margin-top: 0;">💡 Tips for Best Results</h4>
    <ul style="color: #cbd5e1; line-height: 1.8;">
    <li>📷 Use clear, well-lit photos</li>
    <li>🌳 Include leaves and branches in the photo</li>
    <li>📐 Capture the tree from multiple angles for better accuracy</li>
    <li>🎯 Avoid shadows and reflections</li>
    <li>📌 Photos of 2-5MB work best</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
