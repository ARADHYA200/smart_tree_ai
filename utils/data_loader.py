"""
Data Loader Module - Handles loading and processing tree data
"""
import json
import pandas as pd
import os
from typing import List, Dict, Any
import streamlit as st

@st.cache_resource
def load_trees_data() -> List[Dict[str, Any]]:
    """
    Load and merge tree data from both India and US datasets
    Returns combined dataset with country field added
    """
    try:
        # Load India trees
        india_path = os.path.join(os.path.dirname(__file__), "..", "data", "india.json")
        with open(india_path, 'r', encoding='utf-8') as f:
            india_trees = json.load(f)
        
        for tree in india_trees:
            tree['country'] = 'India'
        
        # Load US trees
        us_path = os.path.join(os.path.dirname(__file__), "..", "data", "us.json")
        with open(us_path, 'r', encoding='utf-8') as f:
            us_trees = json.load(f)
        
        for tree in us_trees:
            tree['country'] = 'US'
        
        # Merge datasets
        all_trees = india_trees + us_trees
        
        # Normalize data
        all_trees = normalize_trees(all_trees)
        
        return all_trees
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return []

def normalize_trees(trees: List[Dict]) -> List[Dict]:
    """
    Normalize tree data structure
    """
    normalized = []
    
    for i, tree in enumerate(trees):
        normalized_tree = {
            'id': i,
            'name': str(tree.get('name', 'Unknown')).title(),
            'scientific_name': str(tree.get('scientific_name', 'N/A')),
            'purpose': tree.get('purpose', ['oxygen']) if isinstance(tree.get('purpose'), list) else ['oxygen'],
            'space': tree.get('space', 'medium'),
            'climate': tree.get('climate', 'hot'),
            'oxygen': int(tree.get('oxygen', 5)),
            'uses': str(tree.get('uses', 'General')),
            'region': str(tree.get('region', 'Unknown')),
            'growth_rate': tree.get('growth_rate', 'medium'),
            'image': str(tree.get('image', 'https://via.placeholder.com/300x300?text=Tree')),
            'country': tree.get('country', 'Unknown'),
            'height': tree.get('height', 'Medium'),
            'water_needs': tree.get('water_needs', 'Moderate'),
            'lifespan': tree.get('lifespan', 'Long'),
        }
        normalized.append(normalized_tree)
    
    return normalized

@st.cache_data
def get_unique_values(trees: List[Dict], field: str) -> List[str]:
    """Get unique values for a field"""
    values = set()
    for tree in trees:
        val = tree.get(field, '')
        if val and val != 'Unknown':
            if isinstance(val, list):
                values.update(val)
            else:
                values.add(str(val))
    return sorted(list(values))

def filter_trees(trees: List[Dict], 
                country: str = None,
                climate: str = None,
                purpose: str = None,
                space: str = None,
                search_text: str = None) -> List[Dict]:
    """
    Filter trees based on criteria
    """
    filtered = trees.copy()
    
    if country and country != 'All Countries':
        filtered = [t for t in filtered if t['country'] == country]
    
    if climate and climate != 'All Climates':
        filtered = [t for t in filtered if t['climate'] == climate]
    
    if space and space != 'All Sizes':
        filtered = [t for t in filtered if t['space'] == space]
    
    if purpose and purpose != 'All Purposes':
        filtered = [t for t in filtered if purpose in t['purpose']]
    
    if search_text:
        search_lower = search_text.lower()
        filtered = [t for t in filtered if 
                   search_lower in t['name'].lower() or 
                   search_lower in t['scientific_name'].lower()]
    
    return filtered

def get_recommendations(trees: List[Dict],
                       purpose: str = 'oxygen',
                       space: str = 'medium',
                       climate: str = 'hot',
                       country: str = 'India') -> List[Dict]:
    """
    Smart recommendation engine - scores trees based on criteria
    """
    recommendations = []
    
    for tree in trees:
        score = 0
        max_score = 0
        
        # Purpose matching (40 points)
        if purpose in tree['purpose']:
            score += 40
        else:
            score += 10
        max_score += 40
        
        # Space matching (30 points)
        if tree['space'] == space:
            score += 30
        elif tree['space'] in ['medium'] if space in ['small', 'large'] else ['small', 'large']:
            score += 15
        max_score += 30
        
        # Climate matching (30 points)
        if tree['climate'] == climate:
            score += 30
        else:
            score += 10
        max_score += 30
        
        # Country preference (10 points)
        if tree['country'] == country:
            score += 10
        max_score += 10
        
        # Calculate percentage
        score_pct = (score / max_score) * 100
        
        recommendations.append({
            **tree,
            'match_score': score_pct
        })
    
    # Sort by score descending
    recommendations = sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
    
    return recommendations[:10]  # Return top 10

def get_statistics(trees: List[Dict]) -> Dict[str, Any]:
    """Get dashboard statistics"""
    stats = {
        'total_trees': len(trees),
        'avg_oxygen': round(sum(t['oxygen'] for t in trees) / len(trees), 1) if trees else 0,
        'unique_countries': len(set(t['country'] for t in trees)),
        'unique_purposes': len(set(p for t in trees for p in t['purpose'])),
        'climate_distribution': {},
        'space_distribution': {},
        'country_count': {}
    }
    
    for tree in trees:
        # Climate distribution
        climate = tree['climate']
        stats['climate_distribution'][climate] = stats['climate_distribution'].get(climate, 0) + 1
        
        # Space distribution
        space = tree['space']
        stats['space_distribution'][space] = stats['space_distribution'].get(space, 0) + 1
        
        # Country count
        country = tree['country']
        stats['country_count'][country] = stats['country_count'].get(country, 0) + 1
    
    return stats
