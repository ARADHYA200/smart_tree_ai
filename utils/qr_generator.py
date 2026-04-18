"""
QR Code Generator Module
"""
import qrcode
import io
# from PIL import Image
import base64
from typing import Tuple

from config import config

def generate_qr_code(tree_name: str, tree_id: int, size: int = 10) -> Image.Image:
    """
    Generate QR code for a tree
    
    Args:
        tree_name: Name of the tree
        tree_id: ID of the tree
        size: Size of QR code box
    
    Returns:
        PIL Image object
    """
    # Create a URL that QR scanners will recognize immediately
    base_url = config.APP_BASE_URL.rstrip('/')
    url = f"{base_url}/?tree={tree_id}&name={tree_name.replace(' ', '+')}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create a clean, self-contained QR image without external image embedding
    img = qr.make_image(fill_color="black", back_color="white")
    if hasattr(img, 'convert'):
        img = img.convert('RGB')
    return img

def qr_to_bytes(qr_image: Image.Image) -> io.BytesIO:
    """
    Convert QR image to bytes
    """
    img_byte_arr = io.BytesIO()
    qr_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def qr_to_base64(qr_image: Image.Image) -> str:
    """
    Convert QR image to base64 string for embedding in HTML
    """
    img_byte_arr = io.BytesIO()
    qr_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode()
    return f"data:image/png;base64,{img_base64}"

def get_qr_download_link(qr_image: Image.Image, tree_name: str) -> bytes:
    """
    Get downloadable QR code
    """
    buf = io.BytesIO()
    qr_image.save(buf, format='PNG')
    buf.seek(0)
    return buf.getvalue()
