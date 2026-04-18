"""
Data preparation script
Copies and processes data from parent directory to data folder
Run this before first use: python prepare_data.py
"""
import json
import shutil
import os
import sys

def prepare_data():
    """Prepare data for the application"""
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, 'data')
    parent_dir = os.path.dirname(script_dir)
    
    # Create data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    print("🔄 Preparing data files...")
    
    # Copy India trees
    india_src = os.path.join(parent_dir, 'india_trees_100_plus.json')
    india_dst = os.path.join(data_dir, 'india.json')
    
    if os.path.exists(india_src):
        with open(india_src, 'r', encoding='utf-8') as f:
            india_data = json.load(f)
        
        with open(india_dst, 'w', encoding='utf-8') as f:
            json.dump(india_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ India trees: {len(india_data)} records copied")
    else:
        print(f"⚠️  Could not find {india_src}")
        # Create dummy data
        create_sample_india_data(india_dst)
    
    # Copy US trees
    us_src = os.path.join(parent_dir, 'us_trees_500.json')
    us_dst = os.path.join(data_dir, 'us.json')
    
    if os.path.exists(us_src):
        with open(us_src, 'r', encoding='utf-8') as f:
            us_data = json.load(f)
        
        with open(us_dst, 'w', encoding='utf-8') as f:
            json.dump(us_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ US trees: {len(us_data)} records copied")
    else:
        print(f"⚠️  Could not find {us_src}")
        # Create dummy data
        create_sample_us_data(us_dst)
    
    print("\n✨ Data preparation complete!")

def create_sample_india_data(filepath):
    """Create sample India data if source not available"""
    sample_data = [
        {
            "name": "Peepal",
            "scientific_name": "Ficus religiosa",
            "purpose": ["oxygen"],
            "space": "large",
            "climate": "hot",
            "oxygen": 6,
            "uses": "Environmental and spiritual benefits",
            "region": "India",
            "growth_rate": "slow",
            "image": "https://via.placeholder.com/300x300?text=Peepal"
        },
        {
            "name": "Neem",
            "scientific_name": "Azadirachta indica",
            "purpose": ["medicinal", "oxygen"],
            "space": "large",
            "climate": "hot",
            "oxygen": 9,
            "uses": "Medicinal and pest control",
            "region": "India",
            "growth_rate": "fast",
            "image": "https://via.placeholder.com/300x300?text=Neem"
        },
        {
            "name": "Ashoka",
            "scientific_name": "Saraca asoca",
            "purpose": ["decorative", "medicinal"],
            "space": "medium",
            "climate": "hot",
            "oxygen": 7,
            "uses": "Ornamental and medicinal uses",
            "region": "India",
            "growth_rate": "medium",
            "image": "https://via.placeholder.com/300x300?text=Ashoka"
        }
    ]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Created sample India data: {filepath}")

def create_sample_us_data(filepath):
    """Create sample US data if source not available"""
    sample_data = [
        {
            "name": "Oak",
            "scientific_name": "Quercus robur",
            "purpose": ["oxygen"],
            "space": "large",
            "climate": "cold",
            "oxygen": 8,
            "uses": "Shade and oxygen production",
            "region": "USA",
            "growth_rate": "slow",
            "image": "https://via.placeholder.com/300x300?text=Oak"
        },
        {
            "name": "Maple",
            "scientific_name": "Acer saccharum",
            "purpose": ["oxygen", "decorative"],
            "space": "large",
            "climate": "cold",
            "oxygen": 7,
            "uses": "Shade tree with beautiful fall colors",
            "region": "USA",
            "growth_rate": "medium",
            "image": "https://via.placeholder.com/300x300?text=Maple"
        },
        {
            "name": "Pine",
            "scientific_name": "Pinus sylvestris",
            "purpose": ["oxygen"],
            "space": "large",
            "climate": "cold",
            "oxygen": 6,
            "uses": "Shade and windbreak",
            "region": "USA",
            "growth_rate": "fast",
            "image": "https://via.placeholder.com/300x300?text=Pine"
        }
    ]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Created sample US data: {filepath}")

if __name__ == "__main__":
    prepare_data()
