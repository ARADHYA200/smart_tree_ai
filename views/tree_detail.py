"""
Tree Detail Page
"""
import streamlit as st
from components.cards import render_tree_card
from utils.data_loader import load_trees_data
from utils.qr_generator import generate_qr_code, qr_to_bytes


def render_tree_detail():
    """Render detailed tree information for a scanned QR code."""
    params = st.experimental_get_query_params()
    tree_id_param = params.get("tree", [None])[0]

    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">🌳 Tree Detail</h1>
    <p style="color: #94a3b8; font-size: 14px;">View detailed information for the selected tree.</p>
    """, unsafe_allow_html=True)

    if not tree_id_param:
        st.warning("No tree ID found in the URL. Please use a valid tree QR code.")
        return

    try:
        tree_id = int(tree_id_param)
    except ValueError:
        st.error("Invalid tree ID. Please use a valid QR code or tree link.")
        return

    trees = load_trees_data()
    tree = next((t for t in trees if t["id"] == tree_id), None)

    if tree is None:
        st.error("Tree not found. The tree ID may be invalid or not available in the current dataset.")
        return

    col1, col2 = st.columns([2, 1])

    with col1:
        try:
            st.image(tree["image"], use_column_width=True)
        except Exception:
            st.markdown(
                """
                <div style="background: rgba(6,182,212,0.1); min-height: 240px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #94a3b8;">
                Image unavailable
                </div>
                """,
                unsafe_allow_html=True,
            )

        render_tree_card(tree)

    with col2:
        st.markdown("##### Quick Tree Facts")
        st.markdown(f"**Scientific Name:** {tree['scientific_name']}  \n")
        st.markdown(f"**Country:** {tree['country']}  \n")
        st.markdown(f"**Climate:** {tree['climate'].title()}  \n")
        st.markdown(f"**Space:** {tree['space'].title()}  \n")
        st.markdown(f"**Oxygen Production:** {tree['oxygen']}/10  \n")
        st.markdown(f"**Water Needs:** {tree.get('water_needs', 'Moderate')}  \n")
        st.markdown(f"**Growth Rate:** {tree.get('growth_rate', 'medium').title()}  \n")
        st.markdown(f"**Lifespan:** {tree.get('lifespan', 'Long')}  \n")
        st.markdown(f"**Uses:** {tree.get('uses', 'General')}  \n")

        try:
            qr_img = generate_qr_code(tree['name'], tree['id'])
            st.markdown("##### QR Code")
            st.image(qr_img, width=180)
            buf = qr_to_bytes(qr_img)
            st.download_button(
                label="⬇️ Download QR",
                data=buf,
                file_name=f"tree_{tree['id']}_qr.png",
                mime="image/png",
                key=f"detail_qr_{tree['id']}"
            )
        except Exception:
            st.info("QR generation unavailable")
