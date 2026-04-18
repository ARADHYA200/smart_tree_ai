"""
__init__.py - Pages package initialization
"""

from .dashboard import render_dashboard
from .garden import render_garden
from .image_ai import render_image_ai
from .recommendation import render_recommendations
from .chatbot import render_chatbot

__all__ = [
    "render_dashboard",
    "render_garden",
    "render_image_ai",
    "render_recommendations",
    "render_chatbot",
]
