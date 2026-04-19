"""
Image Classification Module - Tree Detection from Images
Uses CLIP embeddings or simple image similarity matching
"""
import numpy as np
from PIL import Image
import io
from typing import List, Dict, Tuple, Any
import streamlit as st
import hashlib

def cosine_similarity_manual(a, b):
    a = np.array(a)
    b = np.array(b)

    denom = (np.linalg.norm(a) * np.linalg.norm(b)) + 1e-8
    return np.dot(a, b) / denom

class TreeImageClassifier:
    """
    Tree image classifier using image feature extraction and similarity matching
    Lightweight approach using PIL and numpy
    """
    
    def __init__(self):
        """Initialize classifier"""
        self.feature_cache = {}
    
    def extract_image_features(self, image: Image.Image) -> np.ndarray:
        """
        Extract simple features from image
        Uses histogram and basic statistics
        """
        # Resize image for consistency
        image = image.resize((224, 224))
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array
        img_array = np.array(image).astype(float) / 255.0
        
        # Flatten
        img_flat = img_array.flatten()
        
        # Create feature vector from:
        # 1. Color histogram
        hist_r = np.histogram(img_array[:, :, 0], bins=32)[0]
        hist_g = np.histogram(img_array[:, :, 1], bins=32)[0]
        hist_b = np.histogram(img_array[:, :, 2], bins=32)[0]
        
        # 2. Mean colors
        mean_color = [img_array[:, :, i].mean() for i in range(3)]
        
        # 3. Variance
        variance = [img_array[:, :, i].var() for i in range(3)]
        
        # Combine features
        features = np.concatenate([hist_r, hist_g, hist_b, mean_color, variance])
        
        return features / (np.linalg.norm(features) + 1e-8)
    
    def get_url_image_features(self, image_url: str):
        try:
            import requests
            response = requests.get(image_url, timeout=5)
            
            if response.status_code != 200:
                return None
            
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            return self.extract_image_features(image)
        
        except Exception:
            return None   # ❗ REMOVE st.warning spam
    
    def predict_tree(self, 
                    user_image: Image.Image,
                    trees_data: List[Dict],
                    top_k: int = 5) -> List[Tuple[Dict, float]]:
        """
        Predict tree from user uploaded image
        
        Args:
            user_image: PIL Image from user upload
            trees_data: List of tree dictionaries with image URLs
            top_k: Number of top predictions to return
        
        Returns:
            List of (tree_dict, confidence) tuples
        """
        # Extract features from user image
        user_features = self.extract_image_features(user_image)
        
        similarities = []
        
        for tree in trees_data:
            try:
                # Get or cache tree image features
                image_url = tree.get('image', '')
                cache_key = hashlib.md5(image_url.encode()).hexdigest()
                
                if cache_key in self.feature_cache:
                    tree_features = self.feature_cache[cache_key]
                else:
                    tree_features = self.get_url_image_features(image_url)
                    if tree_features is not None:
                        self.feature_cache[cache_key] = tree_features
                
                if tree_features is not None:
                    # Calculate cosine similarity
                    sim = cosine_similarity_manual(user_features, tree_features)
                    
                    # Scale to 0-100
                    confidence = max(0, min(100, (sim + 1) / 2 * 100))
                    similarities.append((tree, confidence))
            
            except Exception as e:
                continue
        
        # Sort by confidence and return top_k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]

class SimpleTreeMatcher:
    """
    Simpler tree matching based on metadata
    Useful when image URLs are not available
    """
    
    @staticmethod
    def match_by_description(description: str, trees: List[Dict]) -> List[Tuple[Dict, float]]:
        """
        Match trees by text description
        """
        matches = []
        description_lower = description.lower()
        
        for tree in trees:
            score = 0
            
            # Check name match
            if tree['name'].lower() in description_lower:
                score += 50
            
            # Check scientific name match
            if tree['scientific_name'].lower() in description_lower:
                score += 40
            
            # Check characteristics
            if tree['climate'] in description_lower:
                score += 20
            
            if tree['space'] in description_lower:
                score += 15
            
            if any(p.lower() in description_lower for p in tree['purpose']):
                score += 15
            
            if score > 0:
                matches.append((tree, min(100, score)))
        
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:5]
