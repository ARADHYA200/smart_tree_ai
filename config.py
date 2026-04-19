"""
Configuration Module - All app settings in one place
"""
import os
from dataclasses import dataclass

@dataclass
class Config:
    """Application configuration"""
    
    # App Info
    APP_NAME = "Smart Tree AI Pro"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "Ultra-advanced tree intelligence platform"
    
    # Server
    SERVER_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", 8501))
    SERVER_ADDRESS = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")
    APP_BASE_URL = os.getenv("APP_BASE_URL", "https://smart-tree-system.streamlit.app")
    
    # Data
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    INDIA_DATA = os.path.join(DATA_DIR, "india.json")
    US_DATA = os.path.join(DATA_DIR, "us.json")
    DATA_CACHE_MINUTES = int(os.getenv("DATA_CACHE_MINUTES", 60))
    
    # UI/UX
    THEME_PRIMARY = "#06b6d4"
    THEME_SECONDARY = "#2563eb"
    THEME_BG_DARK = "#0f172a"
    THEME_BG_DARKER = "#020617"
    THEME_TEXT = "#e2e8f0"
    
    # Performance
    PAGINATION_SIZE = int(os.getenv("PAGINATION_SIZE", 12))
    MAX_UPLOAD_SIZE_MB = int(os.getenv("MAX_UPLOAD_SIZE_MB", 200))
    IMAGE_CACHE_SIZE = int(os.getenv("IMAGE_CACHE_SIZE", 100))
    
    # Features
    ENABLE_IMAGE_AI = os.getenv("ENABLE_IMAGE_AI", "true").lower() == "true"
    ENABLE_CHATBOT = os.getenv("ENABLE_CHATBOT", "true").lower() == "true"
    ENABLE_RECOMMENDATIONS = os.getenv("ENABLE_RECOMMENDATIONS", "true").lower() == "true"
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
    
    # Constants
    OXYGEN_SCALE = 10
    MAX_RECOMMENDATIONS = 10
    TOP_K_IMAGE_PREDICTIONS = 5
    QR_SIZE = 10
    QR_BORDER = 2

# Export config
config = Config()

if __name__ == "__main__":
    print(f"{config.APP_NAME} v{config.APP_VERSION}")
    print(f"Data dir: {config.DATA_DIR}")
    print(f"Server: {config.SERVER_ADDRESS}:{config.SERVER_PORT}")
