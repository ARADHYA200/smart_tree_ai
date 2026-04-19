"""
Chatbot Page - AI-powered tree expert chatbot
"""
import streamlit as st
from utils.data_loader import load_trees_data


def render_chatbot():
    """Render AI chatbot page"""

    st.markdown("""
    <h1 style="color: #e2e8f0;">💬 Tree Expert Chatbot</h1>
    <p style="color: #94a3b8;">Ask me anything about trees 🌳</p>
    """, unsafe_allow_html=True)

    trees = load_trees_data()

    # ✅ INIT STATE
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {
                'role': 'assistant',
                'message': "Hello! I'm your tree expert 🌳 Ask me anything!"
            }
        ]

    if 'chatbot_input' not in st.session_state:
        st.session_state.chatbot_input = ""

    # ✅ SHOW CHAT
    st.markdown("<br>", unsafe_allow_html=True)
    for item in st.session_state.chat_history:
        if item['role'] == 'assistant':
            st.markdown(f"🤖 {item['message']}")
        else:
            st.markdown(f"👤 {item['message']}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ✅ INPUT (FIXED)
    user_input = st.text_input(
        "Your question...",
        key="chatbot_input"
    )

    # ✅ SEND BUTTON
    if st.button("Send"):
        if user_input.strip():
            st.session_state.chat_history.append({
                'role': 'user',
                'message': user_input
            })

            response = generate_chatbot_response(user_input, trees)

            st.session_state.chat_history.append({
                'role': 'assistant',
                'message': response
            })

            st.session_state.chatbot_input = ""
            st.rerun()

    # ✅ SUGGESTIONS (FIXED UX)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Quick Questions")

    suggestions = [
        "What are the best oxygen-producing trees?",
        "How do I care for medicinal trees?",
        "What trees grow in hot climates?",
        "Tell me about native trees in India",
        "How do trees help the environment?",
        "Best trees for small spaces?"
    ]

    cols = st.columns(2)

    for idx, suggestion in enumerate(suggestions):
        with cols[idx % 2]:
            if st.button(f"💭 {suggestion}", key=f"suggest_{idx}"):
                # ✅ Fill input instead of auto-answer
                st.session_state.chatbot_input = suggestion
                st.rerun()


def generate_chatbot_response(user_input: str, trees: list) -> str:
    user_lower = user_input.lower()

    responses = {
        "oxygen": f"Our database has {len([t for t in trees if t['oxygen'] >= 8])} high oxygen-producing trees like Peepal 🌿 and Neem 🌱.",
        "medicinal": f"We have {len([t for t in trees if 'medicinal' in t['purpose']])} medicinal trees used in traditional medicine.",
        "climate": "Choose trees based on your climate 🌤️ — hot vs cold matters a lot!",
        "care": "Tree care includes watering 💧, sunlight ☀️, soil 🌱, and maintenance ✂️.",
        "native": f"India has {len([t for t in trees if t['country'] == 'India'])} native trees 🌳 in our dataset.",
        "environment": "Trees produce oxygen 🌿, absorb CO₂ 🌍, and protect soil.",
        "small": "For small spaces 🏡, choose compact trees like Arjun.",
        "decorative": f"We have {len([t for t in trees if 'decorative' in t['purpose']])} decorative trees 🌸."
    }

    for keyword, response in responses.items():
        if keyword in user_lower:
            return response

    if "?" in user_input:
        return "Try asking about oxygen, medicinal, climate, or native trees 🌳"
    else:
        return "Please ask a specific question about trees 🌱"


    



# """
# Chatbot Page - AI-powered tree expert chatbot
# """
# import streamlit as st
# from utils.data_loader import load_trees_data

# def render_chatbot():
#     """Render AI chatbot page"""

    
#     st.markdown("""
#     <h1 style="color: #e2e8f0; margin-bottom: 10px;">💬 Tree Expert Chatbot</h1>
#     <p style="color: #94a3b8; font-size: 14px;">Ask me anything about trees 🌳</p>
#     """, unsafe_allow_html=True)

#     trees = load_trees_data()

#     # Initialize state
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = [
#             {
#                 'role': 'assistant',
#                 'message': "Hello! I'm your tree expert 🌳 Ask me anything!"
#             }
#         ]

#     if 'chat_input' not in st.session_state:
#         st.session_state.chat_input = ""

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Chat history
#     for item in st.session_state.chat_history:
#         if item['role'] == 'assistant':
#             st.markdown(f"""
#             <div style="background: rgba(6,182,212,0.15); padding:10px; border-radius:8px; margin:5px;">
#             🤖 {item['message']}
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div style="background: rgba(37,99,235,0.15); padding:10px; border-radius:8px; margin:5px;">
#             👤 {item['message']}
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Input
#     user_input = st.text_input("Your question...", key="chat_input")

#     if st.button("Send"):
#         if user_input:
#             st.session_state.chat_history.append({'role': 'user', 'message': user_input})
#             response = generate_chatbot_response(user_input, trees)
#             st.session_state.chat_history.append({'role': 'assistant', 'message': response})
#             st.session_state.chat_input = ""
#             st.rerun()

#     # Suggestions
#     st.markdown("##### Quick Questions")

#     suggestions = [
#         "Best oxygen trees",
#         "Medicinal trees",
#         "Trees for hot climate",
#         "Native trees India",
#         "Small space trees",
#     ]

#     cols = st.columns(2)
#     for i, suggestion in enumerate(suggestions):
#         with cols[i % 2]:
#             if st.button(f"💭 {suggestion}", key=f"suggest_{i}"):
#                 st.session_state.chat_history.append({'role': 'user', 'message': suggestion})
#                 response = generate_chatbot_response(suggestion, trees)
#                 st.session_state.chat_history.append({'role': 'assistant', 'message': response})
#                 st.rerun()


# def generate_chatbot_response(user_input: str, trees: list) -> str:
#     user = user_input.lower()

    
#     if "oxygen" in user or "oxy" in user:
#         return "🌿 Best oxygen producing trees:\n- Peepal\n- Neem\n- Banyan\n- Ashoka"

#     elif "medicinal" in user or "medicine" in user:
#         return "🌱 Medicinal trees:\n- Neem\n- Tulsi\n- Amla\n- Arjun"

#     elif "climate" in user or "hot" in user:
#         return "☀️ Trees for hot climate:\n- Neem\n- Babool\n- Gulmohar"

#     elif "india" in user:
#         return "🇮🇳 Native Indian trees:\n- Banyan\n- Peepal\n- Neem"

#     elif "small" in user:
#         return "🏡 Small space trees:\n- Arjun\n- Champa\n- Guava"

#     elif "environment" in user:
#         return "🌍 Trees help by producing oxygen, absorbing CO2, and supporting life."

#     else:
#         return "🌳 Ask about oxygen, medicinal, climate, or types of trees!"
    
