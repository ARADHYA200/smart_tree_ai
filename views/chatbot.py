# """
# Chatbot Page - AI-powered tree expert chatbot
# Uses OpenAI API for natural conversations about trees
# """
# import streamlit as st
# from utils.data_loader import load_trees_data

# def render_chatbot():
#     """Render AI chatbot page"""
    
#     st.markdown("""
#     <h1 style="color: #e2e8f0; margin-bottom: 10px;">💬 Tree Expert Chatbot</h1>
#     <p style="color: #94a3b8; font-size: 14px;">Ask me anything about trees, gardening, and sustainability</p>
#     """, unsafe_allow_html=True)
    
#     # Load trees data for context
#     trees = load_trees_data()
    
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = [
#             {
#                 'role': 'assistant',
#                 'message': "Hello! I'm your tree expert. I can help you with information about tree species, care tips, environmental benefits, and planting advice. What would you like to know?"
#             }
#         ]

#     if 'chatbot_suggestion' not in st.session_state:
#         st.session_state.chatbot_suggestion = ''

#     st.markdown("<br>", unsafe_allow_html=True)
    
#     # Chat history display
#     history_container = st.container()
#     for item in st.session_state.chat_history:
#         if item['role'] == 'assistant':
#             history_container.markdown(f"""
#             <div style="background: rgba(6,182,212,0.15); border-left: 4px solid #06b6d4; 
#                         padding: 12px 16px; border-radius: 8px; margin: 12px 0;">
#             <p style="color: #cbd5e1; margin: 0;"><strong>🤖 Assistant:</strong> {item['message']}</p>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             history_container.markdown(f"""
#             <div style="background: rgba(37,99,235,0.16); border-left: 4px solid #2563eb; 
#                         padding: 12px 16px; border-radius: 8px; margin: 12px 0;">
#             <p style="color: #cbd5e1; margin: 0;"><strong>You:</strong> {item['message']}</p>
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Chat input form
#     with st.form("chatbot_form", clear_on_submit=False):
#         user_input = st.text_input(
#             "Your question...",
#             placeholder="Ask me about trees, gardening, climate, etc.",
#             key="chatbot_input",
#             value=st.session_state.chatbot_suggestion
#         )
#         submitted = st.form_submit_button("Send")

#     if submitted and user_input:
#         st.session_state.chat_history.append({'role': 'user', 'message': user_input})
#         response = generate_chatbot_response(user_input, trees)
#         st.session_state.chat_history.append({'role': 'assistant', 'message': response})
#         st.session_state.chatbot_suggestion = ''
#         st.rerun()

#     # Quick suggestions
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.markdown("##### Quick Questions")
    
#     suggestions = [
#         "What are the best oxygen-producing trees?",
#         "How do I care for medicinal trees?",
#         "What trees grow in hot climates?",
#         "Tell me about native trees in India",
#         "How do trees help the environment?",
#         "Best trees for small spaces?"
#     ]
    
#     cols = st.columns(2)
#     for idx, suggestion in enumerate(suggestions):
#         with cols[idx % 2]:
#             if st.button(f"💭 {suggestion}", key=f"suggest_{idx}"):
#                 st.session_state.chatbot_suggestion = suggestion
#                 st.rerun()

# def generate_chatbot_response(user_input: str, trees: list) -> str:
#     """
#     Generate chatbot response
#     Uses pattern matching and tree database context
#     """
#     user_lower = user_input.lower()
    
#     # Response library
#     responses = {
#         "oxygen": f"Our database has {len([t for t in trees if t['oxygen'] >= 8])} high oxygen-producing trees. Trees like Peepal and Neem are particularly known for excellent oxygen production.",
#         "medicinal": f"We have {len([t for t in trees if 'medicinal' in t['purpose']])} medicinal trees in our database. They provide health benefits and are used in traditional medicine.",
#         "climate": "Choose trees that match your climate! Hot climate trees are different from cold climate trees. I can recommend the best trees for your specific climate zone.",
#         "care": "Tree care depends on the species, but generally includes: regular watering, proper sunlight, soil preparation, and seasonal maintenance. Which tree would you like care tips for?",
#         "native": f"India has {len([t for t in trees if t['country'] == 'India'])} native trees in our database, while the US has {len([t for t in trees if t['country'] == 'US'])} trees. Native trees thrive best in their regions!",
#         "environment": "Trees are crucial for the environment! They produce oxygen, absorb CO2, prevent soil erosion, and provide habitats. Planting trees is one of the best ways to help our planet.",
#         "small": "For small spaces, consider compact trees like Arjun or trees with limited growth. They provide benefits without taking up too much room.",
#         "decorative": f"We have {len([t for t in trees if 'decorative' in t['purpose']])} ornamental trees perfect for beautifying your garden. Amaltas is a popular decorative choice!",
#     }
    
#     # Check for keywords
#     for keyword, response in responses.items():
#         if keyword in user_lower:
#             return response
    
#     # Default response
#     if "?" in user_input:
#         return "That's a great question! I'm continuously learning about trees. You might want to search our database for specific tree information or ask about a particular tree species. What specific tree or topic interests you?"
#     else:
#         return "I'd be happy to help! Can you please ask me a specific question about trees, gardening, climate, or environmental topics?"


"""
Chatbot Page - AI-powered tree expert chatbot
"""
import streamlit as st
from utils.data_loader import load_trees_data

def render_chatbot():
    """Render AI chatbot page"""

    
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">💬 Tree Expert Chatbot</h1>
    <p style="color: #94a3b8; font-size: 14px;">Ask me anything about trees 🌳</p>
    """, unsafe_allow_html=True)

    trees = load_trees_data()

    # Initialize state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {
                'role': 'assistant',
                'message': "Hello! I'm your tree expert 🌳 Ask me anything!"
            }
        ]

    if 'chat_input' not in st.session_state:
        st.session_state.chat_input = ""

    st.markdown("<br>", unsafe_allow_html=True)

    # Chat history
    for item in st.session_state.chat_history:
        if item['role'] == 'assistant':
            st.markdown(f"""
            <div style="background: rgba(6,182,212,0.15); padding:10px; border-radius:8px; margin:5px;">
            🤖 {item['message']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background: rgba(37,99,235,0.15); padding:10px; border-radius:8px; margin:5px;">
            👤 {item['message']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Input
    user_input = st.text_input("Your question...", key="chat_input")

    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append({'role': 'user', 'message': user_input})
            response = generate_chatbot_response(user_input, trees)
            st.session_state.chat_history.append({'role': 'assistant', 'message': response})
            st.session_state.chat_input = ""
            st.rerun()

    # Suggestions
    st.markdown("##### Quick Questions")

    suggestions = [
        "Best oxygen trees",
        "Medicinal trees",
        "Trees for hot climate",
        "Native trees India",
        "Small space trees",
    ]

    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(f"💭 {suggestion}", key=f"suggest_{i}"):
                st.session_state.chat_history.append({'role': 'user', 'message': suggestion})
                response = generate_chatbot_response(suggestion, trees)
                st.session_state.chat_history.append({'role': 'assistant', 'message': response})
                st.rerun()


def generate_chatbot_response(user_input: str, trees: list) -> str:
    user = user_input.lower()

    
    if "oxygen" in user or "oxy" in user:
        return "🌿 Best oxygen producing trees:\n- Peepal\n- Neem\n- Banyan\n- Ashoka"

    elif "medicinal" in user or "medicine" in user:
        return "🌱 Medicinal trees:\n- Neem\n- Tulsi\n- Amla\n- Arjun"

    elif "climate" in user or "hot" in user:
        return "☀️ Trees for hot climate:\n- Neem\n- Babool\n- Gulmohar"

    elif "india" in user:
        return "🇮🇳 Native Indian trees:\n- Banyan\n- Peepal\n- Neem"

    elif "small" in user:
        return "🏡 Small space trees:\n- Arjun\n- Champa\n- Guava"

    elif "environment" in user:
        return "🌍 Trees help by producing oxygen, absorbing CO2, and supporting life."

    else:
        return "🌳 Ask about oxygen, medicinal, climate, or types of trees!"
    
