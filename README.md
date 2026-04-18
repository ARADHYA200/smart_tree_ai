"""
Smart Tree AI Pro - Setup Instructions & Documentation
"""

# ============================================
# 📋 SETUP INSTRUCTIONS
# ============================================

## 1. Initial Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Prepare Data
```bash
python prepare_data.py
```
This will copy tree data files and prepare them for the application.

### Step 3: Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 2. Project Structure

```
smart_tree_ai_pro/
│
├── app.py                          # Main Streamlit application
├── prepare_data.py                 # Data preparation script
├── requirements.txt                # Python dependencies
│
├── components/
│   ├── sidebar.py                  # Navigation sidebar
│   └── cards.py                    # Card components (UI)
│
├── pages/
│   ├── dashboard.py                # Dashboard with KPIs
│   ├── garden.py                   # Tree browser with filters
│   ├── image_ai.py                 # Image recognition page
│   ├── recommendation.py           # Smart recommendations
│   └── chatbot.py                  # AI chatbot
│
├── utils/
│   ├── data_loader.py              # Data loading & processing
│   └── qr_generator.py             # QR code generation
│
├── model/
│   └── image_classifier.py         # Image classification model
│
├── assets/
│   └── styles.css                  # Custom CSS styles
│
└── data/
    ├── india.json                  # India trees dataset
    └── us.json                     # US trees dataset
```

---

## 3. Features Guide

### 📊 Dashboard
- Real-time statistics
- KPI metrics (Total trees, Avg oxygen, etc.)
- Climate distribution charts
- Space requirement analysis
- Country distribution

### 🌳 Garden
- Browse 600+ trees
- Search by name or scientific name
- Filter by: Country, Climate, Space, Purpose
- Pagination for performance
- Download QR codes for each tree
- Add to favorites

### 🤖 Image AI
- Upload tree photos
- AI recognizes tree species
- Shows top 5 matches with confidence scores
- Displays tree details and QR codes
- Full tree information for each match

### 💡 Recommendations
- Answer 4 simple questions
- Get personalized tree recommendations
- See match score for each recommendation
- Based on: Purpose, Space, Climate, Country

### 💬 Chatbot
- Ask questions about trees
- Get care tips
- Learn environmental benefits
- Quick suggestions for common queries

### ⭐ Favorites
- Save favorite trees
- Access your saved selections later

### ⚙️ Settings
- Theme preferences
- Data management
- About & Information

---

## 4. Key Technologies

- **Frontend**: Streamlit (Modern web framework)
- **Backend**: Python 3.8+
- **Data**: JSON (600+ trees)
- **Visualization**: Plotly (Interactive charts)
- **ML/AI**: Image classification, similarity matching
- **Styling**: Custom CSS + HTML

---

## 5. Performance Optimizations

- ✅ Data caching with @st.cache_resource
- ✅ Pagination (12 trees per page)
- ✅ Lazy loading of images
- ✅ Session state management
- ✅ Efficient filtering algorithms
- ✅ Feature caching for image classification

---

## 6. Configuration

### Environment Variables (Optional)
```bash
export OPENAI_API_KEY="your-key-here"  # For chatbot enhancement
```

### Settings Location
All settings can be modified in `⚙️ Settings` page within the app.

---

## 7. Troubleshooting

### App won't start?
```bash
# Clear Streamlit cache
streamlit cache clear

# Then run again
streamlit run app.py
```

### Data not loading?
```bash
# Re-prepare data
python prepare_data.py
```

### Images not loading?
- Check internet connection (images loaded from URLs)
- Placeholders will show if images unavailable

### Performance issues?
- Data is automatically cached
- Try reducing filters or search scope
- Restart the app: `streamlit run app.py`

---

## 8. Customization Guide

### Adding More Trees
Edit `data/india.json` or `data/us.json`:
```json
{
  "name": "Tree Name",
  "scientific_name": "Scientific Name",
  "purpose": ["oxygen", "medicinal"],
  "space": "small|medium|large",
  "climate": "hot|cold",
  "oxygen": 1-10,
  "uses": "Description",
  "region": "Location",
  "growth_rate": "slow|medium|fast",
  "image": "URL or path to image"
}
```

### Changing Colors
Modify the CSS in `app.py`:
- Primary color: `#06b6d4` (Cyan)
- Secondary color: `#2563eb` (Blue)
- Background: `#0f172a` to `#020617` (Dark)

### Adding New Pages
1. Create new file in `pages/`
2. Implement `render_[page_name]()` function
3. Add to sidebar in `components/sidebar.py`
4. Add route in `app.py`

---

## 9. API Integration (Future)

### OpenAI Integration
```python
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": user_input}]
)
```

### Enhanced Image Classification
Can integrate with:
- Google Vision API
- AWS Rekognition
- Azure Computer Vision

---

## 10. Deployment

### Deploy to Streamlit Cloud
1. Push code to GitHub
2. Go to share.streamlit.io
3. Select your repository
4. App deployed!

### Deploy to AWS/GCP/Azure
- Dockerfile is compatible with containerization
- Requires: Python 3.8+, pip install -r requirements.txt
- Run: `streamlit run app.py --server.port 8501`

---

## 11. Support & Contributing

- Report issues via GitHub Issues
- Submit feature requests
- Contribute improvements via Pull Requests

---

## 12. License & Credits

Smart Tree AI Pro v1.0
Built for Tree Enthusiasts & Environmentalists
🌿 Making a Greener Tomorrow 🌿

---

## 13. Quick Start Commands

```bash
# Complete setup
python prepare_data.py && streamlit run app.py

# Development with auto-reload
streamlit run app.py --logger.level=debug

# Production mode
streamlit run app.py --logger.level=error --client.toolbarMode="minimal"

# Clear cache and restart
streamlit cache clear && streamlit run app.py
```

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Production Ready ✅

