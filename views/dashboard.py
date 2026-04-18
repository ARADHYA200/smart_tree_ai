"""
Dashboard Page - KPI metrics, charts and analytics
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.data_loader import load_trees_data, get_statistics
from components.cards import render_metric_card, render_kpi_row

def render_dashboard():
    """Render main dashboard with metrics and charts"""
    
    st.markdown("""
    <h1 style="color: #e2e8f0; margin-bottom: 10px;">📊 Dashboard</h1>
    <p style="color: #94a3b8; font-size: 14px;">Real-time tree database analytics and insights</p>
    """, unsafe_allow_html=True)
    
    # Load data
    trees = load_trees_data()
    stats = get_statistics(trees)
    
    # KPI Cards
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_metric_card(
            title="Total Trees",
            value=f"{stats['total_trees']:,}",
            subtitle="in database",
            icon="🌳"
        )
    
    with col2:
        render_metric_card(
            title="Avg Oxygen",
            value=f"{stats['avg_oxygen']:.1f}/10",
            subtitle="production",
            icon="🌱"
        )
    
    with col3:
        render_metric_card(
            title="Countries",
            value=stats['unique_countries'],
            subtitle="covered",
            icon="🌍"
        )
    
    with col4:
        render_metric_card(
            title="Purposes",
            value=stats['unique_purposes'],
            subtitle="identified",
            icon="🎯"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts Row 1
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); 
                    border: 1px solid rgba(6,182,212,0.2); padding: 20px; border-radius: 12px;">
        """, unsafe_allow_html=True)
        
        st.markdown("##### Climate Distribution")
        
        climate_data = stats['climate_distribution']
        fig = go.Figure(data=[go.Pie(
            labels=list(climate_data.keys()),
            values=list(climate_data.values()),
            marker=dict(colors=['#06b6d4', '#f59e0b', '#2563eb']),
        )])
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', size=12),
            showlegend=True,
            height=300,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with chart_col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); 
                    border: 1px solid rgba(6,182,212,0.2); padding: 20px; border-radius: 12px;">
        """, unsafe_allow_html=True)
        
        st.markdown("##### Space Distribution")
        
        space_data = stats['space_distribution']
        fig = go.Figure(data=[go.Bar(
            y=list(space_data.keys()),
            x=list(space_data.values()),
            orientation='h',
            marker=dict(color='#06b6d4'),
        )])
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', size=12),
            showlegend=False,
            height=300,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False)
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Country Distribution
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); 
                border: 1px solid rgba(6,182,212,0.2); padding: 20px; border-radius: 12px;">
    """, unsafe_allow_html=True)
    
    st.markdown("##### Country Distribution")
    
    country_data = stats['country_count']
    fig = go.Figure(data=[go.Bar(
        x=list(country_data.keys()),
        y=list(country_data.values()),
        marker=dict(
            color=list(country_data.values()),
            colorscale='Viridis',
        ),
    )])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e2e8f0', size=12),
        showlegend=False,
        height=300,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Summary Section
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(6,182,212,0.1), rgba(37,99,235,0.05));
                backdrop-filter: blur(10px); border: 1px solid rgba(6,182,212,0.2); 
                padding: 20px; border-radius: 12px;">
    <h3 style="color: #e2e8f0; margin-top: 0;">📈 Insights</h3>
    <ul style="color: #cbd5e1; line-height: 1.8;">
        <li>🌍 The database contains trees from {unique_countries} different regions</li>
        <li>🌳 Average oxygen production score: <b>{avg_oxygen:.1f}/10</b></li>
        <li>🎯 Trees serve {unique_purposes} different purposes</li>
        <li>📊 Most common climate type: <b>{most_common_climate}</b></li>
    </ul>
    </div>
    """.format(
        unique_countries=stats['unique_countries'],
        avg_oxygen=stats['avg_oxygen'],
        unique_purposes=stats['unique_purposes'],
        most_common_climate=max(stats['climate_distribution'], key=stats['climate_distribution'].get)
    ), unsafe_allow_html=True)
