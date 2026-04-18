"""
__init__.py - Package initialization
"""

__version__ = "1.0.0"
__author__ = "Smart Tree AI"
__description__ = "Ultra-advanced tree intelligence platform"

# Import main components
from views.dashboard import render_dashboard
from views.garden import render_garden
from views.image_ai import render_image_ai
from views.recommendation import render_recommendations
from views.chatbot import render_chatbot

__all__ = [
    "render_dashboard",
    "render_garden",
    "render_image_ai",
    "render_recommendations",
    "render_chatbot",
]
