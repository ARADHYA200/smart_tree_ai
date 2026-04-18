"""
Card Components - Reusable card UI components
"""
import streamlit as st
from typing import Dict, Any, Optional
import plotly.graph_objects as go

def render_metric_card(title: str, value: Any, subtitle: str = "", icon: str = ""):
    """
    Render a metric card for dashboard
    """
    col = st.container()
    
    with col:
        st.markdown(f"""
        <style>
        .metric-card {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(6,182,212,0.2);
            padding: 20px;
            border-radius: 12px;
            margin: 10px 0;
            transition: all 0.3s ease;
        }}
        .metric-card:hover {{
            border-color: rgba(6,182,212,0.6);
            box-shadow: 0 0 20px rgba(6,182,212,0.2);
            transform: translateY(-2px);
        }}
        .metric-icon {{
            font-size: 32px;
            margin-bottom: 10px;
        }}
        .metric-title {{
            font-size: 14px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin: 0;
        }}
        .metric-value {{
            font-size: 32px;
            font-weight: bold;
            color: #06b6d4;
            margin: 10px 0;
        }}
        .metric-subtitle {{
            font-size: 12px;
            color: #64748b;
        }}
        </style>
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <p class="metric-title">{title}</p>
            <p class="metric-value">{value}</p>
            <p class="metric-subtitle">{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)

def render_tree_card(tree: Dict[str, Any], show_qr: bool = False, qr_image = None):
    """
    Render a tree card with details
    """
    st.markdown(f"""
    <style>
    .tree-card {{
        background: linear-gradient(135deg, rgba(6,182,212,0.1), rgba(37,99,235,0.05));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(6,182,212,0.2);
        padding: 16px;
        border-radius: 12px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }}
    .tree-card:hover {{
        border-color: rgba(6,182,212,0.6);
        box-shadow: 0 0 20px rgba(6,182,212,0.2);
        transform: translateY(-4px);
    }}
    .tree-name {{
        font-size: 18px;
        font-weight: bold;
        color: #e2e8f0;
        margin-bottom: 8px;
    }}
    .tree-scientific {{
        font-size: 12px;
        color: #94a3b8;
        font-style: italic;
        margin-bottom: 12px;
    }}
    .tree-badge {{
        display: inline-block;
        padding: 4px 10px;
        background: rgba(6,182,212,0.2);
        border-radius: 6px;
        font-size: 11px;
        color: #06b6d4;
        margin-right: 6px;
        margin-bottom: 8px;
    }}
    .tree-stat {{
        font-size: 13px;
        color: #cbd5e1;
        margin: 6px 0;
    }}
    .oxygen-bar {{
        width: 100%;
        height: 6px;
        background: rgba(255,255,255,0.1);
        border-radius: 3px;
        overflow: hidden;
        margin-top: 8px;
    }}
    .oxygen-fill {{
        height: 100%;
        background: linear-gradient(90deg, #06b6d4, #2563eb);
    }}
    </style>
    <div class="tree-card">
        <div class="tree-name">{tree['name']}</div>
        <div class="tree-scientific">{tree['scientific_name']}</div>
        <div>
            <span class="tree-badge">🌍 {tree['country']}</span>
            <span class="tree-badge">🌡️ {tree['climate'].title()}</span>
            <span class="tree-badge">📏 {tree['space'].title()}</span>
        </div>
        <div class="tree-stat">🌱 Climate: {tree['climate'].title()}</div>
        <div class="tree-stat">📍 Region: {tree['region']}</div>
        <div class="tree-stat">⏱️ Growth: {tree['growth_rate'].title()}</div>
        <div class="tree-stat">💧 Purpose: {', '.join([p.title() for p in tree['purpose']])}</div>
        <div style="margin-top: 10px;">
            <div style="font-size: 12px; color: #94a3b8; margin-bottom: 4px;">Oxygen Production: {tree['oxygen']}/10</div>
            <div class="oxygen-bar">
                <div class="oxygen-fill" style="width: {tree['oxygen'] * 10}%"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if show_qr and qr_image:
        col1, col2 = st.columns([3, 1])
        with col2:
            st.image(qr_image, width=120)

def render_recommendation_card(tree: Dict[str, Any], score: float):
    """
    Render recommendation card with match score
    """
    score_color = "#06b6d4" if score >= 70 else "#f59e0b" if score >= 50 else "#ef4444"
    
    st.markdown(f"""
    <style>
    .rec-card {{
        background: linear-gradient(135deg, rgba(6,182,212,0.05), rgba(37,99,235,0.03));
        backdrop-filter: blur(10px);
        border-left: 4px solid {score_color};
        padding: 16px;
        border-radius: 8px;
        margin: 12px 0;
    }}
    .rec-name {{
        font-size: 16px;
        font-weight: bold;
        color: #e2e8f0;
    }}
    .rec-score {{
        font-size: 28px;
        font-weight: bold;
        color: {score_color};
        margin: 10px 0;
    }}
    .rec-stat {{
        font-size: 12px;
        color: #cbd5e1;
        margin: 4px 0;
    }}
    </style>
    <div class="rec-card">
        <div class="rec-name">{tree['name']}</div>
        <div class="rec-score">{score:.1f}% Match</div>
        <div class="rec-stat">🌍 {tree['country']} • 🌡️ {tree['climate']}</div>
        <div class="rec-stat">📏 {tree['space']} • ⏱️ {tree['growth_rate']}</div>
    </div>
    """, unsafe_allow_html=True)

def render_kpi_row(kpis: Dict[str, Any]):
    """
    Render row of KPI cards
    """
    cols = st.columns(len(kpis))
    
    for col, (label, value) in zip(cols, kpis.items()):
        with col:
            render_metric_card(
                title=label.split("|")[0].strip(),
                value=value,
                subtitle=label.split("|")[1].strip() if "|" in label else "",
                icon="📊"
            )
